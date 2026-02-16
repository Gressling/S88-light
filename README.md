# S88-light

An open XML/JSON vocabulary for process chemistry recipes, inspired by ISA-88/IEC 61512.

[![DOI](https://zenodo.org/badge/664350527.svg)](https://zenodo.org/badge/latestdoi/664350527)
![GitHub commits since latest release (by SemVer including pre-releases)](https://img.shields.io/github/commits-since/Gressling/S88/3-alpha)
![GitHub contributors](https://img.shields.io/github/contributors/Gressling/S88)
![GitHub issues](https://img.shields.io/github/issues/Gressling/S88)

This namespace dictionary further develops many flavours of today's XML-based batch standards. It focuses on labs, experiments, semi-batch environments, and data-science usability. It is formed along **five dimensions**:

1. **Operation** — unit operations (the atomic actions)
2. **Order (Sequence)** — recipe workflow and orchestration
3. **Event (Time)** — recorded time series and observations
4. **Device** — hardware declarations
5. **Material** — chemical and ingredient declarations

## Design Principles

It **is**: easy to read, de-normalised (linear), lab-worker authored, vendor-agnostic, data-science friendly, declarative.

It is **not**: a reactor management system, a programming language, an IT system perspective, or a full ISA-88 implementation.

You always need an IT system to generate or run S88-light, for example [openReactor](https://github.com/Gressling/openReactor).

## Repository Structure

```
s88-light.xsd                          Unified XML Schema (all operations + orchestration)
s88-light.schema.json                  Equivalent JSON Schema (2020-12)
examples/                              Validated example recipes (XML + JSON)
dimensions/
├── 1_operations/                      [1] Unit Operations
│   ├── api/                              Process operations (16)
│   ├── manual/                           Human-in-the-loop steps (9)
│   ├── analytics/                        PAT, IPC (2)
│   ├── formulation/                      Coating, granulation (3)
│   └── elementary/                       Generic building blocks (6)
├── 2_sequence/                        [2] Workflow and Recipe
├── 3_events/                          [3] Events, TimeSeries, Observations
├── 4_devices/                         [4] Hardware declarations
└── 5_materials/                       [5] Ingredient declarations
ontology/                              Concept maps (heat transfer, mass transfer)
use-cases/                             Applied examples (cost calc, ELN, XDL transforms)
labforward-s88/                        Python library for Laboperator API
xml/                                   Versioned schemas and XSLT transformations
docs/                                  Specification and reference
```

## Quick Start

```xml
<Recipe xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        xsi:noNamespaceSchemaLocation="s88-light.xsd">
  <Metadata><Name>Aspirin Synthesis</Name></Metadata>
  <Sequence>
    <Prepare device="R-101">
      <Chemical><Name>Toluol</Name><Amount unit="mL">250</Amount></Chemical>
    </Prepare>
    <Stirring><StirringSpeed unit="RPM">500</StirringSpeed></Stirring>
    <Temperature><TargetTemperature unit="°C">50</TargetTemperature></Temperature>
    <Parallel>
      <AddOnce>
        <Chemical><Name>Acetic anhydride</Name><Amount unit="mL">5</Amount></Chemical>
      </AddOnce>
      <AddOnce>
        <Chemical><Name>Salicylic acid</Name><Amount unit="g">4</Amount></Chemical>
      </AddOnce>
    </Parallel>
  </Sequence>
</Recipe>
```

## Documentation

| Document | Contents |
|---|---|
| **[Wiki](https://github.com/Gressling/S88-light/wiki)** | Canonical reference with per-operation pages |
| [dimensions/](dimensions/) | Five-dimension index (mirrors wiki sidebar) |
| [docs/specification.md](docs/specification.md) | Schema specification: data model, types, orchestration |
| [docs/operations.md](docs/operations.md) | Tabular unit-operation reference |
| [docs/json-format.md](docs/json-format.md) | JSON format and mapping rules |
| [CHANGELOG.md](CHANGELOG.md) | Version history |

## Validation

```bash
# XML
python -c "from lxml import etree; s=etree.XMLSchema(etree.parse('s88-light.xsd')); \
  print(s.validate(etree.parse('examples/aspirin-synthesis.xml')))"

# JSON
python -c "import json,jsonschema; jsonschema.validate( \
  json.load(open('examples/aspirin-synthesis.json')), \
  json.load(open('s88-light.schema.json'))); print(True)"
```

## Python Library

See [labforward-s88/](labforward-s88/) for the Laboperator API integration.

## License

MIT — see [LICENSE](LICENSE).

## Citation

If you use S88-light in published work, cite the Zenodo DOI above.

