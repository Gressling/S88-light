# Changelog

All notable changes to this project are documented in this file.  
Format follows [Keep a Changelog](https://keepachangelog.com/).

## [1.1.0] – 2026-02-16

### Added
- **5-dimension directory structure** mirroring the [wiki taxonomy](https://github.com/Gressling/S88-light/wiki):
  - `dimensions/1_operations/` with subcategories: `api/`, `manual/`, `analytics/`, `formulation/`, `elementary/`
  - `dimensions/2_sequence/`, `3_events/`, `4_devices/`, `5_materials/`
- 36 per-operation README.md pages following wiki standard (Description, Example, Ontology)
- 12 new operation stubs: Extraction, Solvent, PAT, IPC, RollerCompactor, Coating, FluidBedGranulator, EmptyOperation, GenericActor, GenericSensor, ManualInput, EventRecorder, SingleSpectrum
- Dimension index pages (`dimensions/README.md`, per-dimension READMEs)

### Changed
- Operations reorganized from flat `operations/` into categorized `dimensions/1_operations/{api,manual,analytics,formulation,elementary}/`
- Root `README.md`: updated to 5-dimension structure, wiki link as canonical reference
- `docs/specification.md`: added 5-dimension table, operation category breakdown
- `docs/operations.md`: expanded from 24 to 36 operations with category headers
- `dimensions/3_events/README.md`: rewritten concisely with Event, TimeSeries, Eventframe examples
- Fixed typo: `Destillation/` → `Distillation/`

### Removed
- Flat `operations/` directory (content moved to `dimensions/1_operations/`)
- Flat `events/` directory (content moved to `dimensions/3_events/`)

## [1.0.0] – 2025-01-01

### Added
- Unified XML Schema (`s88-light.xsd`) with 24 unit operations, typed quantities, `Parallel`/`Loop` orchestration, and `Recipe` root element
- JSON Schema (`s88-light.schema.json`, draft 2020-12) with `if/then` discriminated unions
- Example recipes: `examples/aspirin-synthesis.xml`, `examples/aspirin-synthesis.json`
- Documentation: `docs/specification.md`, `docs/operations.md`, `docs/json-format.md`
- Rewritten Python library (`labforward-s88/`) with `S88Config`, token caching, `build_json()`, validation helpers

### Fixed
- `setup.py`: removed stdlib modules from `install_requires`
- `.env` template: removed hardcoded credentials; added `S88_TENANT`, `S88_OAUTH_URL`
- `events/README.md`: corrected malformed namespace prefixes
- `dimensions/sequence/README.md`: replaced invalid XML with valid recipe example

### Changed
- Root `README.md`: scientific rewrite with quick-start examples, validation commands, and citation block
- Python module: `S88_TENANT` env var replaces hardcoded tenant; no module-level side effects; proper error handling

### Removed
- Old `labforward-s88-light.py` (replaced by `s88_light.py`)
- Dummy `README.txt` in `labforward-s88/`

## [0.x] – Pre-release

Individual XSD files per operation without a unified schema. No JSON support. Python module with hardcoded credentials.
