"""
S88-light: Python library for Laboperator API integration and S88 recipe generation.

Provides functions for:
- Authenticating with Laboperator OAuth 2.0
- Retrieving workflow run and measurement data
- Building S88-light XML recipes from API data
- Building S88-light JSON recipes from API data
- Exporting to pandas DataFrames / CSV

Configuration is loaded from environment variables (CLIENT_ID, CLIENT_SECRET, etc.)
or can be passed explicitly to functions.
"""

import http.client
import urllib.parse
import base64
import json
import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom
import pandas as pd
from datetime import datetime
import os
import logging

logger = logging.getLogger("s88_light")


# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

class S88Config:
    """
    Holds API configuration. Reads from environment variables by default,
    but all values can be overridden at construction time.
    """

    def __init__(
        self,
        oauth_url: str = None,
        client_id: str = None,
        client_secret: str = None,
        tenant: str = None,
    ):
        self.oauth_url = oauth_url or os.environ.get("S88_OAUTH_URL", os.environ.get("API_BASE_URL", "laboperator.labforward.app"))
        self.client_id = client_id or os.environ.get("CLIENT_ID")
        self.client_secret = client_secret or os.environ.get("CLIENT_SECRET")
        self.tenant = tenant or os.environ.get("S88_TENANT", "labforward")
        self._access_token = None

        # Strip protocol prefix if present — http.client needs bare hostname
        for prefix in ("https://", "http://"):
            if self.oauth_url.startswith(prefix):
                self.oauth_url = self.oauth_url[len(prefix):]

    def validate(self):
        """Raise ValueError if required credentials are missing."""
        if not self.client_id:
            raise ValueError("CLIENT_ID is not set. Provide it via environment variable or S88Config(client_id=...)")
        if not self.client_secret:
            raise ValueError("CLIENT_SECRET is not set. Provide it via environment variable or S88Config(client_secret=...)")

    @property
    def access_token(self):
        """Get or lazily refresh the OAuth access token (cached)."""
        if self._access_token is None:
            self._access_token = _request_token(self)
        return self._access_token

    def refresh_token(self):
        """Force-refresh the access token."""
        self._access_token = _request_token(self)
        return self._access_token


# Default config — lazily populated from env on first use
_default_config = None


def get_config(**kwargs) -> S88Config:
    """Return the default config singleton, or a custom one if kwargs are provided."""
    global _default_config
    if kwargs:
        return S88Config(**kwargs)
    if _default_config is None:
        _default_config = S88Config()
    return _default_config


# ---------------------------------------------------------------------------
# OAuth 2.0
# ---------------------------------------------------------------------------

class AuthenticationError(Exception):
    """Raised when OAuth token retrieval fails."""
    pass


class APIError(Exception):
    """Raised when an API call returns an unexpected status code."""
    pass


def _request_token(config: S88Config) -> str:
    """
    Retrieve a new access token from the OAuth 2.0 server.

    Parameters:
        config: S88Config instance with oauth_url, client_id, client_secret.

    Returns:
        str: The access token.

    Raises:
        AuthenticationError: If the token request fails.
    """
    config.validate()

    conn = http.client.HTTPSConnection(config.oauth_url)
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Authorization": "Basic " + base64.b64encode(
            f"{config.client_id}:{config.client_secret}".encode()
        ).decode("utf-8"),
    }
    data = urllib.parse.urlencode({"grant_type": "client_credentials"})

    try:
        conn.request("POST", "/oauth/token", body=data, headers=headers)
        response = conn.getresponse()
        body = response.read().decode("utf-8")

        if response.status != 200:
            raise AuthenticationError(
                f"Token request failed (HTTP {response.status}): {body}"
            )

        token_data = json.loads(body)
        if "access_token" not in token_data:
            raise AuthenticationError(
                f"Token response missing 'access_token': {body}"
            )

        return token_data["access_token"]

    except (http.client.HTTPException, ConnectionError, OSError) as exc:
        raise AuthenticationError(f"Connection to {config.oauth_url} failed: {exc}") from exc
    finally:
        conn.close()


# ---------------------------------------------------------------------------
# API Calls
# ---------------------------------------------------------------------------

def _api_get(config: S88Config, path: str) -> dict:
    """
    Make an authenticated GET request to the Laboperator API.

    Returns:
        dict: Parsed JSON response.

    Raises:
        APIError: If the request fails.
    """
    conn = http.client.HTTPSConnection(config.oauth_url)
    headers = {
        "Accept": "application/vnd.api+json",
        "Authorization": f"Bearer {config.access_token}",
    }
    try:
        conn.request("GET", path, headers=headers)
        response = conn.getresponse()
        body = response.read().decode("utf-8")

        if response.status != 200:
            raise APIError(f"API GET {path} failed (HTTP {response.status}): {body}")

        return json.loads(body)

    except (http.client.HTTPException, ConnectionError, OSError) as exc:
        raise APIError(f"Connection to {config.oauth_url}{path} failed: {exc}") from exc
    finally:
        conn.close()


def get_workflow_run_data(workflow_run_id: str, config: S88Config = None) -> dict:
    """
    Retrieve data for a Laboperator workflow run.

    Parameters:
        workflow_run_id: The ID of the workflow run.
        config: Optional S88Config; uses default if not provided.

    Returns:
        dict: The full JSON response as a dict.
    """
    cfg = config or get_config()
    path = f"/api/v2/{cfg.tenant}/workflow_runs/{workflow_run_id}?template=true"
    return _api_get(cfg, path)


def get_measurement_data(measurement_id: str, config: S88Config = None) -> dict:
    """
    Retrieve measurement data including data points.

    Parameters:
        measurement_id: The ID of the measurement.
        config: Optional S88Config; uses default if not provided.

    Returns:
        dict: The full JSON response as a dict.
    """
    cfg = config or get_config()
    path = f"/api/v2/{cfg.tenant}/measurements/{measurement_id}?data_points=true&locale=en"
    return _api_get(cfg, path)


# ---------------------------------------------------------------------------
# Data helpers
# ---------------------------------------------------------------------------

def remove_line_breaks(d):
    """Recursively replace newlines with spaces in all string values of a dict."""
    for k, v in d.items():
        if isinstance(v, dict):
            remove_line_breaks(v)
        elif isinstance(v, str):
            d[k] = v.replace("\n", " ")
        elif isinstance(v, list):
            for i, val in enumerate(v):
                if isinstance(val, dict):
                    remove_line_breaks(val)
                elif isinstance(val, str):
                    v[i] = val.replace("\n", " ")


def dict_to_element(tag: str, d: dict) -> ET.Element:
    """
    Convert a dictionary to an XML element tree.

    - dict values → child elements (recursive)
    - list values → repeated child elements
    - scalar values → child elements with text content (not attributes)
    """
    elem = ET.Element(tag)
    for key, value in d.items():
        if isinstance(value, dict):
            child = dict_to_element(key, value)
            elem.append(child)
        elif isinstance(value, list):
            for item in value:
                if isinstance(item, dict):
                    child = dict_to_element(key, item)
                    elem.append(child)
                else:
                    item_elem = ET.SubElement(elem, key)
                    item_elem.text = str(item)
        else:
            child = ET.SubElement(elem, key)
            child.text = str(value) if value is not None else ""
    return elem


def format_seconds(seconds: float) -> str:
    """Format seconds as hh:mm:ss."""
    hours, remainder = divmod(seconds, 3600)
    minutes, secs = divmod(remainder, 60)
    return f"{int(hours):02d}:{int(minutes):02d}:{int(secs):02d}"


def _extract_measurement_channels(measurement_dict: dict):
    """
    Extract channel data points from a measurement API response.

    Returns:
        list[dict]: One entry per channel with keys: channel_id, data_points, min_timestamp.
    """
    if "data" not in measurement_dict or "attributes" not in measurement_dict["data"]:
        return []

    data_points = measurement_dict["data"]["attributes"].get("data_points", [])
    if not data_points:
        return []

    channels = {}
    for dp in data_points:
        ch_id, ts, val = dp[0], dp[1], dp[2]
        if ch_id not in channels:
            channels[ch_id] = {"channel_id": ch_id, "data_points": [], "min_timestamp": ts}
        channels[ch_id]["data_points"].append((ts, val))
        if ts < channels[ch_id]["min_timestamp"]:
            channels[ch_id]["min_timestamp"] = ts

    return list(channels.values())


# ---------------------------------------------------------------------------
# Build XML output
# ---------------------------------------------------------------------------

def build_xml(workflow_run_id: str, measurement_ids: list, xml_filename: str, config: S88Config = None):
    """
    Build an S88-light XML file from a Laboperator workflow run and measurements.

    Parameters:
        workflow_run_id: The workflow run ID.
        measurement_ids: List of measurement IDs to include.
        xml_filename: Output file path.
        config: Optional S88Config.
    """
    cfg = config or get_config()

    # Fetch workflow data
    workflow_data = get_workflow_run_data(workflow_run_id, cfg)
    remove_line_breaks(workflow_data)

    # Build XML tree
    experiment = ET.Element("Experiment")
    workflow_elem = dict_to_element("WorkflowRun", workflow_data)
    experiment.append(workflow_elem)

    # Add measurements as Trend elements
    for mid in measurement_ids:
        mdata = get_measurement_data(mid, cfg)
        measurement_id_str = mdata.get("data", {}).get("id", mid)
        channels = _extract_measurement_channels(mdata)

        if not channels:
            logger.warning(f"Measurement {mid}: no data points found, skipping.")
            continue

        trend = ET.SubElement(experiment, "Trend", name=str(measurement_id_str))
        data_elem = ET.SubElement(trend, "Data")

        for ch in channels:
            ch_elem = ET.SubElement(data_elem, "Channel", id=str(ch["channel_id"]))
            min_ts = datetime.strptime(ch["min_timestamp"], "%Y-%m-%dT%H:%M:%S.%fZ")
            sorted_pts = sorted(ch["data_points"], key=lambda x: x[0])

            for ts_str, value in sorted_pts:
                ts = datetime.strptime(ts_str, "%Y-%m-%dT%H:%M:%S.%fZ")
                rel = format_seconds((ts - min_ts).total_seconds())
                dp_elem = ET.SubElement(ch_elem, "DataPoint", timestamp=rel)
                dp_elem.text = str(value)

    # Write formatted XML
    xml_bytes = ET.tostring(experiment, encoding="utf-8")
    pretty = minidom.parseString(xml_bytes).toprettyxml(indent="  ")

    with open(xml_filename, "w", encoding="utf-8") as f:
        f.write(pretty)

    logger.info(f"XML saved to {xml_filename}")
    print(f"XML saved to {xml_filename}")


# ---------------------------------------------------------------------------
# Build JSON output
# ---------------------------------------------------------------------------

def build_json(workflow_run_id: str, measurement_ids: list, json_filename: str, config: S88Config = None):
    """
    Build an S88-light JSON file from a Laboperator workflow run and measurements.

    Parameters:
        workflow_run_id: The workflow run ID.
        measurement_ids: List of measurement IDs to include.
        json_filename: Output file path.
        config: Optional S88Config.
    """
    cfg = config or get_config()

    # Fetch workflow data
    workflow_data = get_workflow_run_data(workflow_run_id, cfg)
    remove_line_breaks(workflow_data)

    result = {
        "Experiment": {
            "WorkflowRun": workflow_data,
            "Trends": [],
        }
    }

    for mid in measurement_ids:
        mdata = get_measurement_data(mid, cfg)
        measurement_id_str = mdata.get("data", {}).get("id", mid)
        channels = _extract_measurement_channels(mdata)

        if not channels:
            logger.warning(f"Measurement {mid}: no data points found, skipping.")
            continue

        trend = {"name": str(measurement_id_str), "channels": []}

        for ch in channels:
            min_ts = datetime.strptime(ch["min_timestamp"], "%Y-%m-%dT%H:%M:%S.%fZ")
            sorted_pts = sorted(ch["data_points"], key=lambda x: x[0])
            channel_data = {
                "id": str(ch["channel_id"]),
                "dataPoints": [],
            }
            for ts_str, value in sorted_pts:
                ts = datetime.strptime(ts_str, "%Y-%m-%dT%H:%M:%S.%fZ")
                rel = format_seconds((ts - min_ts).total_seconds())
                channel_data["dataPoints"].append({
                    "timestamp": rel,
                    "value": value,
                })
            trend["channels"].append(channel_data)

        result["Experiment"]["Trends"].append(trend)

    with open(json_filename, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)

    logger.info(f"JSON saved to {json_filename}")
    print(f"JSON saved to {json_filename}")


# ---------------------------------------------------------------------------
# Build DataFrame / CSV output
# ---------------------------------------------------------------------------

def build_dataframe(workflow_run_id: str, measurement_ids: list, output_csv_filename: str, config: S88Config = None):
    """
    Extract measurement data into a pandas DataFrame and save as CSV.

    Parameters:
        workflow_run_id: The workflow run ID.
        measurement_ids: List of measurement IDs.
        output_csv_filename: Output CSV file path.
        config: Optional S88Config.
    """
    cfg = config or get_config()
    df_list = []

    for mid in measurement_ids:
        mdata = get_measurement_data(mid, cfg)
        measurement_id_str = mdata.get("data", {}).get("id", mid)
        data_points = mdata.get("data", {}).get("attributes", {}).get("data_points", [])

        if not data_points:
            logger.warning(f"Measurement {mid}: no data points found, skipping.")
            continue

        mdf = pd.DataFrame(data_points, columns=["channel_id", "timestamp", "value"])
        mdf["timestamp"] = pd.to_datetime(mdf["timestamp"])
        min_ts = mdf["timestamp"].min()
        mdf["relative_timestamp"] = mdf["timestamp"] - min_ts
        mdf["measurement_id"] = measurement_id_str
        df_list.append(mdf)

    if not df_list:
        logger.warning("No data points found across any measurements.")
        print("Warning: No data points found across any measurements.")
        return

    result_df = pd.concat(df_list, ignore_index=True)
    result_df["relative_timestamp"] = result_df["relative_timestamp"].apply(
        lambda x: format_seconds(x.total_seconds())
    )
    result_df.to_csv(output_csv_filename, index=False)

    logger.info(f"DataFrame saved to {output_csv_filename}")
    print(f"DataFrame saved to {output_csv_filename}")


# ---------------------------------------------------------------------------
# Convenience: validate against schemas
# ---------------------------------------------------------------------------

def validate_xml_against_xsd(xml_path: str, xsd_path: str) -> bool:
    """
    Validate an XML file against an XSD schema.

    Requires lxml. Returns True if valid, False if not.
    Prints validation errors to stderr.
    """
    try:
        from lxml import etree
    except ImportError:
        raise ImportError("lxml is required for XML validation. Install with: pip install lxml")

    with open(xsd_path, "r", encoding="utf-8") as f:
        schema_doc = etree.parse(f)
    schema = etree.XMLSchema(schema_doc)

    with open(xml_path, "r", encoding="utf-8") as f:
        xml_doc = etree.parse(f)

    is_valid = schema.validate(xml_doc)
    if not is_valid:
        for error in schema.error_log:
            logger.error(f"Validation error: {error}")
            print(f"Validation error: {error}")
    return is_valid


def validate_json_against_schema(json_path: str, schema_path: str) -> bool:
    """
    Validate a JSON file against a JSON Schema.

    Requires jsonschema. Returns True if valid, False if not.
    """
    try:
        import jsonschema
    except ImportError:
        raise ImportError("jsonschema is required for JSON validation. Install with: pip install jsonschema")

    with open(schema_path, "r", encoding="utf-8") as f:
        schema = json.load(f)
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    try:
        jsonschema.validate(instance=data, schema=schema)
        return True
    except jsonschema.ValidationError as exc:
        logger.error(f"JSON validation error: {exc.message}")
        print(f"JSON validation error: {exc.message}")
        return False
