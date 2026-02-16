# JSON Format

This document describes the JSON representation of S88-light recipes, validated by `s88-light.schema.json` (JSON Schema 2020-12).

## Structure

```json
{
  "Metadata": { "Name": "...", "Version": "...", ... },
  "Sequence": [ <Step>, <Step>, ... ]
}
```

`Metadata` is optional. `Sequence` is required and non-empty.

## Steps

Each step is an object with a discriminator field `operation`:

```json
{ "operation": "AddOnce", "parameters": { ... } }
```

Special step types:

```json
{ "operation": "Parallel", "steps": [ <Step>, ... ] }
{ "operation": "Loop", "iterations": 5, "breakCondition": "...", "body": [ <Step>, ... ] }
```

## Parameters

Operation-specific fields are placed inside the `parameters` object. Field names match the XML element names exactly.

## Quantity Objects

Physical quantities that are elements with a `unit` attribute in XML become objects in JSON:

| XML | JSON |
|---|---|
| `<Amount unit="mL">50</Amount>` | `{"value": 50, "unit": "mL"}` |
| `<Duration unit="s">600</Duration>` | `{"value": 600, "unit": "s"}` |
| `<TargetTemperature unit="°C">80</TargetTemperature>` | `{"value": 80, "unit": "°C"}` |

`FlexibleQuantityType` additionally allows a plain string:

```json
"RateOfAddition": "All at once"
```

## Chemicals

```json
{
  "Name": "Sulfuric acid",
  "Amount": { "value": 10, "unit": "mL" },
  "CAS": "7664-93-9",
  "Role": "Catalyst"
}
```

`Name` and `Amount` are required; `CAS`, `MolWeight`, and `Role` are optional.

## Discriminated Unions

The JSON Schema uses `allOf` with `if/then/const` blocks to enforce operation-specific parameter constraints. This replaces the simpler `oneOf` pattern, which fails when multiple operation schemas contain only optional fields.

```json
{
  "allOf": [
    {
      "if": { "properties": { "operation": { "const": "Stirring" } } },
      "then": { "properties": { "parameters": { "$ref": "#/$defs/StirringParams" } } }
    }
  ]
}
```

## Validation

```bash
pip install jsonschema
python -c "
import json, jsonschema
schema = json.load(open('s88-light.schema.json'))
doc = json.load(open('examples/aspirin-synthesis.json'))
jsonschema.validate(doc, schema)
print('valid')
"
```
