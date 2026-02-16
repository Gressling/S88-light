# labforward-s88-light

Python library for integrating with the [Laboperator](https://www.labforward.io/laboperator/) API and generating S88-light recipe files in XML and JSON format.

## Installation

```bash
pip install -e .

# With validation support (lxml + jsonschema):
pip install -e ".[validation]"
```

## Configuration

Copy `labforward/s88_light.env` to `.env` in your working directory and fill in your credentials:

```dotenv
CLIENT_ID="your-client-id"
CLIENT_SECRET="your-client-secret"
S88_OAUTH_URL=laboperator.labforward.app
S88_TENANT=labforward
```

Or pass them programmatically:

```python
from labforward.s88_light import S88Config, build_xml, build_json

config = S88Config(
    oauth_url="laboperator.labforward.app",
    client_id="...",
    client_secret="...",
    tenant="labforward",
)
```

## Usage

### Build XML from Laboperator data
```python
from labforward.s88_light import build_xml

build_xml(
    workflow_run_id="abc-123",
    measurement_ids=["meas-1", "meas-2"],
    xml_filename="output.xml",
)
```

### Build JSON from Laboperator data
```python
from labforward.s88_light import build_json

build_json(
    workflow_run_id="abc-123",
    measurement_ids=["meas-1", "meas-2"],
    json_filename="output.json",
)
```

### Build DataFrame / CSV
```python
from labforward.s88_light import build_dataframe

build_dataframe(
    workflow_run_id="abc-123",
    measurement_ids=["meas-1", "meas-2"],
    output_csv_filename="output.csv",
)
```

### Validate recipes against schemas
```python
from labforward.s88_light import validate_xml_against_xsd, validate_json_against_schema

# XML validation
valid = validate_xml_against_xsd("recipe.xml", "s88-light.xsd")

# JSON validation
valid = validate_json_against_schema("recipe.json", "s88-light.schema.json")
```

## API Reference

| Function | Description |
|---|---|
| `S88Config(...)` | Configuration object (OAuth URL, credentials, tenant) |
| `get_workflow_run_data(id)` | Fetch workflow run JSON from Laboperator |
| `get_measurement_data(id)` | Fetch measurement JSON with data points |
| `build_xml(...)` | Generate S88-light XML from API data |
| `build_json(...)` | Generate S88-light JSON from API data |
| `build_dataframe(...)` | Generate CSV from measurement data |
| `validate_xml_against_xsd(...)` | Validate XML against XSD schema |
| `validate_json_against_schema(...)` | Validate JSON against JSON Schema |
