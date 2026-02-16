# S88-light Schema Specification

**Version 1.0.0**

## 1. Scope

S88-light defines a minimal XML/JSON schema for batch process chemistry recipes. It captures:

- An ordered sequence of unit operations
- Concurrent (parallel) execution blocks
- Iterative (loop) constructs with break conditions
- Typed physical quantities with explicit units
- Material/chemical specifications

The schema is intentionally limited. It encodes *what* to do and *with what parameters*, not the control logic of *how* equipment executes commands. This distinction follows the ISA-88 separation of procedural control from equipment control.

## 2. Data Model

### 2.1 Recipe

The root element. Contains optional `Metadata` and a required `Sequence`.

| Field | Type | Required | Description |
|---|---|---|---|
| `Metadata` | object | No | Name, version, author, date, description, project |
| `Sequence` | array of Steps | Yes | Ordered list of steps to execute |

### 2.2 Step

A step is one of:

| Variant | Description |
|---|---|
| **Operation** | A single unit operation (e.g., `AddOnce`, `Stirring`) |
| **Parallel** | A set of steps that execute concurrently |
| **Loop** | A repeated block with iteration count and/or break condition |

### 2.3 Unit Operation

Each operation has a fixed tag name (XML) or `operation` string (JSON) and operation-specific parameters. All operations share the optional field `SafetyMeasures` (string).

See [operations.md](operations.md) for the full reference.

### 2.4 Type System

S88-light defines four reusable quantity types. In XML these are expressed as element text with attributes; in JSON as objects.

| Type | XML form | JSON form | Purpose |
|---|---|---|---|
| `QuantityType` | `<Amount unit="ml">250</Amount>` | `{"value": 250, "unit": "ml"}` | Exact numeric quantity with mandatory unit |
| `FlexibleQuantityType` | `<RateOfAddition unit="mL/min">2</RateOfAddition>` | `{"value": 2, "unit": "mL/min"}` or `"All at once"` | Numeric with unit, or descriptive string |
| `TemperatureType` | `<TargetTemperature unit="°C">50</TargetTemperature>` | `{"value": 50, "unit": "°C"}` | Temperature (default unit: °C) |
| `DurationType` | `<Duration unit="s">3600</Duration>` | `{"value": 3600, "unit": "s"}` | Time duration (default unit: s) |

Units are free-form strings. No unit ontology is enforced at the schema level, but SI units or common laboratory conventions (mL, g, RPM, °C, bar) are recommended.

### 2.5 Chemical

Describes a reagent or solvent.

| Field | Type | Required |
|---|---|---|
| `Name` | string | Yes |
| `Amount` | FlexibleQuantityType | Yes |
| `CAS` | string | No |
| `MolWeight` | FlexibleQuantityType | No |
| `Role` | string | No |

## 3. Orchestration

### 3.1 Sequence

Steps in a `Sequence` execute in document order. Each step completes before the next begins, unless wrapped in `Parallel`.

### 3.2 Parallel

All child steps of a `Parallel` block begin simultaneously. The `Parallel` block completes when all children complete.

```xml
<Parallel>
  <AddOnce>...</AddOnce>
  <Stirring>...</Stirring>
</Parallel>
```

### 3.3 Loop

Repeats its `Body` for a fixed number of `Iterations`, until a `BreakCondition` is met, or both (whichever terminates first). At least one of `Iterations` or `BreakCondition` should be provided.

```xml
<Loop>
  <Iterations>10</Iterations>
  <BreakCondition>temperature &gt; 70</BreakCondition>
  <Body>
    <Stirring><StirringSpeed unit="RPM">500</StirringSpeed></Stirring>
  </Body>
</Loop>
```

Break conditions are opaque strings; their evaluation semantics are defined by the executing system.

## 4. Schema Files

| File | Format | Validates |
|---|---|---|
| `s88-light.xsd` | XML Schema 1.0 | XML recipes (`<Recipe>` root) |
| `s88-light.schema.json` | JSON Schema 2020-12 | JSON recipes (top-level object with `Sequence`) |

Both schemas are normative and maintained in parallel. The XML schema is the primary definition; the JSON schema mirrors it structurally.

## 5. Extensibility

New unit operations can be added by:

1. Defining a new `complexType` in `s88-light.xsd`
2. Adding the element to `OperationGroup`
3. Adding the corresponding `*Params` definition and `if/then` clause in `s88-light.schema.json`
4. Adding the operation name to the `enum` in `OperationStep.operation`

Operation parameter sets are intentionally flat (no deep nesting) to support straightforward mapping to tabular formats (CSV, DataFrame).

## 6. Relation to ISA-88

S88-light maps to the ISA-88 procedural model as follows:

| ISA-88 | S88-light |
|---|---|
| Procedure | `Recipe` |
| Unit Procedure | — (not modeled; recipes are single-unit) |
| Operation | `Sequence` step |
| Phase | Unit operation element (e.g., `Stirring`, `AddOnce`) |

S88-light does not model equipment entities, control modules, or state machines.

## 7. Normative References

- ANSI/ISA-88.01-2010, *Batch Control Part 1: Models and Terminology*
- W3C XML Schema 1.0 (Second Edition)
- JSON Schema 2020-12 (draft-bhutton-json-schema-01)
