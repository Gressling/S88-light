import requests
from lxml import etree

def load_xml_from_url(xml_url):
    response = requests.get(xml_url)
    xml_doc = etree.fromstring(response.content)
    return xml_doc

def load_xsd_from_url(xsd_url):
    response = requests.get(xsd_url)
    xsd_doc = etree.fromstring(response.content)
    xsd_schema = etree.XMLSchema(xsd_doc)
    return xsd_schema

# Validates XML against XSD
def validate_xml(xml_doc, xsd_schema):
    is_valid = xsd_schema.validate(xml_doc)
    return is_valid

# Prints result of validation
def print_validation_result(is_valid):
    if is_valid:
        print("The XML is valid against the XSD schema.")
    else:
        print("The XML is not valid against the XSD schema.")
        print(xsd_schema.error_log)

# Load XML document for Absorption
xml_doc = load_xml_from_url("https://raw.githubusercontent.com/Gressling/S88/main/UnitOperations/Absorption/Absorption-test.xml")

# Load XSD framework for Absorption
xsd_schema = load_xsd_from_url("https://raw.githubusercontent.com/Gressling/S88/main/UnitOperations/Absorption/Absorption.xsd")

# Validate the XML against the XSD schema
is_valid = validate_xml(xml_doc, xsd_schema)

# Print validation result
print_validation_result(is_valid)
