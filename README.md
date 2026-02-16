# S88-light

An open, lightweight XML/JSON vocabulary for encoding process chemistry recipes, derived from the ISA-88 batch control standard.

[![DOI](https://zenodo.org/badge/664350527.svg)](https://zenodo.org/badge/latestdoi/664350527)
![GitHub commits since latest release (by SemVer including pre-releases)](https://img.shields.io/github/commits-since/Gressling/S88/3-alpha)
![GitHub contributors](https://img.shields.io/github/contributors/Gressling/S88)
![GitHub issues](https://img.shields.io/github/issues/Gressling/S88)

## Motivation

Laboratory process recipes are routinely recorded as free text, spreadsheets, or proprietary ELN formats. This inhibits reproducibility, automated execution, and cross-platform data exchange. S88-light provides a minimal, schema-validated vocabulary that captures the essential structure of batch chemistry workflows — sequential and parallel unit operations with typed physical quantities — without the complexity of the full ISA-88/IEC 61512 standard.

## Quick Start

A recipe is a `<Recipe>` (XML) or top-level object (JSON) containing a `Sequence` of unit operations:

```xml
<Recipe xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        xsi:noNamespaceSchemaLocation="s88-light.xsd">
  <Metadata>
    <Name>Aspirin Synthesis</Name>
  </Metadata>
  <Sequence>
    <Prepare device="defaultReactor">
      <Chemical><Name>Toluol</Name><Amount unit="ml">250</Amount></Chemical>
    </Prepare>
    <Stirring>
      <StirringSpeed unit="RPM">500</StirringSpeed>
      <StirringDirection>Clockwise</StirringDirection>
    </Stirring>
    <Temperature name="RampUp50">
      <TargetTemperature unit="°C">50</TargetTemperature>
    </Temperature>
    <Parallel>
      <AddOnce>
        <Chemical><Name>Acetic anhydride</Name><Amount unit="ml">5</Amount></Chemical>
        <RateOfAddition unit="mL/min">2</RateOfAddition>
      </AddOnce>
      <AddOnce>
        <Chemical><Name>Salicylic acid</Name><Amount unit="g">4</Amount></Chemical>
        <RateOfAddition unit="g/min">1</RateOfAddition>
      </AddOnce>
    </Parallel>
    <ManualStep>
      <Criteria>Reaction complete (TLC)</Criteria>
    </ManualStep>
  </Sequence>
</Recipe>
```

The equivalent JSON:

```json
{
  "Metadata": { "Name": "Aspirin Synthesis" },
  "Sequence": [
    { "operation": "Prepare", "device": "defaultReactor",
      "parameters": { "Chemicals": [{ "Name": "Toluol", "Amount": { "value": 250, "unit": "ml" } }] } },
    { "operation": "Stirring",
      "parameters": { "StirringSpeed": { "value": 500, "unit": "RPM" }, "StirringDirection": "Clockwise" } },
    { "operation": "Temperature", "name": "RampUp50",
      "parameters": { "TargetTemperature": { "value": 50, "unit": "°C" } } },
    { "parallel": [
        { "operation": "AddOnce", "parameters": { "Chemical": { "Name": "Acetic anhydride", "Amount": { "value": 5, "unit": "ml" } }, "RateOfAddition": { "value": 2, "unit": "mL/min" } } },
        { "operation": "AddOnce", "parameters": { "Chemical": { "Name": "Salicylic acid", "Amount": { "value": 4, "unit": "g" } }, "RateOfAddition": { "value": 1, "unit": "g/min" } } }
    ]},
    { "operation": "ManualStep", "parameters": { "Criteria": "Reaction complete (TLC)" } }
  ]
}
```

## Repository Structure

```
s88-light.xsd              Unified XML Schema (all operations + orchestration)
s88-light.schema.json      Equivalent JSON Schema (2020-12)
examples/                  Validated example recipes (XML + JSON)
docs/                      Specification and reference documentation
operations/                Per-operation XSDs, templates, examples, notebooks
dimensions/                Materials, devices, events, sequence schemas
labforward-s88/            Python library for Laboperator API integration
use-cases/                 Applied examples (cost calc, ELN, XDL transforms)
xml/                       Versioned schemas and XSLT transformations
```

## Documentation

| Document | Contents |
|---|---|
| [docs/specification.md](docs/specification.md) | Schema specification: data model, types, orchestration |
| [docs/operations.md](docs/operations.md) | Unit operation reference (all 24 operations) |
| [docs/json-format.md](docs/json-format.md) | JSON format specification |
| [CHANGELOG.md](CHANGELOG.md) | Version history |

## Validation

```bash
# XML (requires lxml)
python -c "from lxml import etree; s=etree.XMLSchema(etree.parse('s88-light.xsd')); print(s.validate(etree.parse('examples/aspirin-synthesis.xml')))"

# JSON (requires jsonschema)
python -c "import json,jsonschema; jsonschema.validate(json.load(open('examples/aspirin-synthesis.json')),json.load(open('s88-light.schema.json'))); print(True)"
```

## Python Library

See [labforward-s88/README.md](labforward-s88/README.md) for the Laboperator API integration library.

## Contributing

Contributions welcome. Open an issue or pull request.

## License

MIT. See [LICENSE](LICENSE).

## Citation

If you use S88-light in published work, please cite the Zenodo DOI above.

