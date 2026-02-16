# Unit Operation Reference

36 operations are defined across 5 categories. For each, **bold** fields are required; all others are optional. Every operation accepts an optional `SafetyMeasures` (string) unless noted otherwise.

Per-operation pages with examples are in [`dimensions/1_operations/`](../dimensions/1_operations/).

| Category | Operations |
|---|---|
| **API** (16) | Absorption, Centrifugation, Crystallization, Distillation, Dry, Evaporation, Extraction, Fermentation, Filtration, HeatExchange, Temperature, IonExchange, MembraneSeparation, Mixing, Pulverization, Stirring |
| **Manual** (9) | AddOnce, Cleaning, GeneralCleaning, Disposing, Prepare, Setup, Solvent, Washing, Weighing |
| **Analytics** (2) | PAT, IPC |
| **Formulation** (3) | RollerCompactor, Coating, FluidBedGranulator |
| **Elementary** (6) | EmptyOperation, GenericActor, GenericSensor, ManualInput, EventRecorder, SingleSpectrum |

---

# API Operations

## Prepare
Prepare raw materials before processing.

| Field | Type |
|---|---|
| **Chemical** (1..*) | ChemicalType |
| Duration | DurationType |
| Equipment | string |
| *attr* `device` | string |

## AddOnce
Single addition of a chemical to the process.

| Field | Type |
|---|---|
| **Chemical** | ChemicalType |
| Timing | string |
| RateOfAddition | FlexibleQuantityType |
| Temperature | TemperatureType |
| Pressure | FlexibleQuantityType |
| pH | decimal |
| Solvent | string |
| ReactionEnvironment | string |
| Equipment | string |

## Stirring
Mechanical agitation.

| Field | Type |
|---|---|
| **StirringSpeed** | FlexibleQuantityType |
| StirringTime | DurationType |
| StirringDirection | string |
| StirrerDesign | string |
| StirrerSizeAndShape | string |
| ContainerGeometry | string |
| MaterialOfConstruction | string |
| OperationalLimits | string |
| Viscosity | FlexibleQuantityType |
| ShearRate | FlexibleQuantityType |
| AdditionalAgitationMechanisms | string |
| StirringRateProfiles | string |

## Temperature
Heating or cooling to a setpoint.

| Field | Type |
|---|---|
| **TargetTemperature** | TemperatureType |
| Duration | DurationType |
| HeatingRate | FlexibleQuantityType |
| CoolingRate | FlexibleQuantityType |
| Equipment | string |
| *attr* `name` | string |

## Mixing
Combine multiple ingredients.

| Field | Type |
|---|---|
| Ingredients / Ingredient (0..*) | { Name: string, Quantity: FlexibleQuantityType } |
| MixingMethod | string |
| MixingTime | DurationType |
| MixingTemperature | TemperatureType |
| MixingSpeed | FlexibleQuantityType |
| MixingContainer | string |
| InertAtmosphere | boolean |
| PostMixingTreatment | string |
| HomogeneityTesting | string |

## Crystallization
Controlled crystal formation.

| Field | Type |
|---|---|
| **Compound** | string |
| Solvent | string |
| Temperature | TemperatureType |
| CoolingRate | FlexibleQuantityType |
| StirringSpeed | FlexibleQuantityType |
| CrystallizationTime | DurationType |
| SeedCrystal | string |
| CrystalSize | FlexibleQuantityType |
| CrystalShape | string |
| CrystalPurity | FlexibleQuantityType |
| Yield | FlexibleQuantityType |
| pH | decimal |
| Additives | string |
| Equipment | string |

## Distillation
Thermal separation of a liquid mixture.

| Field | Type |
|---|---|
| **Mixture** | string |
| Temperature | TemperatureType |
| Pressure | FlexibleQuantityType |
| HeatingRate | FlexibleQuantityType |
| CoolingRate | FlexibleQuantityType |
| RefluxRatio | FlexibleQuantityType |
| DistillateCollectors | string |
| SolventSelection | string |
| Equipment | string |

## Filtration
Solid–liquid separation through a porous medium.

| Field | Type |
|---|---|
| FilterType | string |
| PoreSize | FlexibleQuantityType |
| FeedSolution | string |
| FiltrationRate | FlexibleQuantityType |
| FilterArea | FlexibleQuantityType |
| FilterCakeThickness | FlexibleQuantityType |
| FiltrationTime | DurationType |
| Temperature | TemperatureType |
| PressureOrVacuum | FlexibleQuantityType |
| PreFiltrationTreatment | string |
| CleaningAndMaintenance | string |
| FiltrationEfficiency | FlexibleQuantityType |
| Equipment | string |

## Centrifugation
Separation by centrifugal force.

| Field | Type |
|---|---|
| **Sample** | string |
| Speed | FlexibleQuantityType |
| Time | DurationType |
| Temperature | TemperatureType |
| Pressure | FlexibleQuantityType |
| RotationDirection | string |
| Equipment | string |

## Evaporation
Solvent removal by vaporisation.

| Field | Type |
|---|---|
| **Product** | string |
| EvaporationMethod | string |
| EvaporationTemperature | TemperatureType |
| EvaporationTime | DurationType |
| Solvent | string |
| Concentration | FlexibleQuantityType |
| HeatingSource | string |
| Equipment | string |

## Dry
Moisture removal from a solid product.

| Field | Type |
|---|---|
| **Product** | string |
| DryingMethod | string |
| DryingTemperature | TemperatureType |
| DryingTime | DurationType |
| Humidity | FlexibleQuantityType |
| AirflowRate | FlexibleQuantityType |
| Equipment | string |

## Fermentation
Microbial or enzymatic biotransformation.

| Field | Type |
|---|---|
| **MicroorganismStrain** | string |
| InoculumSize | FlexibleQuantityType |
| Feedstock | string |
| NutrientComposition | string |
| pH | decimal |
| Temperature | TemperatureType |
| AerationOrOxygenation | string |
| FermentationTime | DurationType |
| AgitationOrMixing | string |
| FermentationVesselType | string |
| ProductRecovery | string |
| YieldAndProductivity | string |

## Absorption
Gas–liquid mass transfer.

| Field | Type |
|---|---|
| **GasStream** | string |
| LiquidPhase | string |
| Solvent | string |
| Temperature | TemperatureType |
| Pressure | FlexibleQuantityType |
| MassTransferCoefficient | FlexibleQuantityType |
| ContactTime | DurationType |
| pH | decimal |
| Equipment | string |

## IonExchange
Ion-exchange chromatography or treatment.

| Field | Type |
|---|---|
| **IonExchangeResinType** | string |
| IonExchangeCapacity | FlexibleQuantityType |
| FeedSolution | string |
| ContactTime | DurationType |
| Temperature | TemperatureType |
| FlowRate | FlexibleQuantityType |
| RegenerationMethod | string |
| pH | decimal |
| Equipment | string |

## MembraneSeparation
Pressure-driven membrane process.

| Field | Type |
|---|---|
| **MembraneType** | string |
| MembraneMaterial | string |
| FeedSolution | string |
| OperatingPressure | FlexibleQuantityType |
| FeedFlowRate | FlexibleQuantityType |
| Temperature | TemperatureType |
| MembraneSurfaceArea | FlexibleQuantityType |
| CleaningAndMaintenance | string |
| Equipment | string |

## Washing
Impurity removal by solvent wash.

| Field | Type |
|---|---|
| **MaterialToBeWashed** | string |
| WashingSolventOrMedium | string |
| WashingTemperature | TemperatureType |
| WashingTime | DurationType |
| NumberOfWashingSteps | integer |
| WashingVolumeOrRatio | FlexibleQuantityType |
| AgitationOrMixing | string |
| Drying | string |
| Equipment | string |

## Pulverization
Size reduction by mechanical grinding.

| Field | Type |
|---|---|
| **FeedMaterial** | string |
| ParticleSizeRequirement | FlexibleQuantityType |
| PulverizationEquipment | string |
| PulverizationTime | DurationType |
| PulverizationSpeed | FlexibleQuantityType |
| CoolingOrHeating | string |
| DustCollection | string |

## Weighing
Mass determination of a substance.

| Field | Type |
|---|---|
| **Substance** | string |
| **Amount** | FlexibleQuantityType |
| BalanceType | string |
| Duration | DurationType |

## HeatExchange
Counter-/co-current heat transfer between two fluid streams.

| Field | Type |
|---|---|
| HotFluid | string |
| ColdFluid | string |
| InletTemperatureHot | TemperatureType |
| InletTemperatureCold | TemperatureType |
| OutletTemperatureHot | TemperatureType |
| OutletTemperatureCold | TemperatureType |
| FlowRateHot | FlexibleQuantityType |
| FlowRateCold | FlexibleQuantityType |
| HeatExchangerType | string |
| Equipment | string |

## Setup
Equipment preparation before the experiment.

| Field | Type |
|---|---|
| ExperimentName | string |
| SetupInstructions | string |
| Duration | DurationType |
| Equipment | string |

## PreCleaning / PostCleaning
Equipment cleaning before or after the process. Both share `CleaningType`.

| Field | Type |
|---|---|
| Materials | string |
| Procedure | string |
| Duration | DurationType |
| Environment | string |

## Disposal
Waste handling and disposal.

| Field | Type |
|---|---|
| **WasteType** | string |
| DisposalMethod | string |
| Amount | FlexibleQuantityType |
| Duration | DurationType |
| Environment | string |

## ManualStep
Human-in-the-loop intervention. Does not carry `SafetyMeasures`.

| Field | Type |
|---|---|
| Description | string |
| Timing | string |
| Criteria | string |

---

# Analytics Operations

## PAT
Process Analytical Technology — in-line or on-line measurement during batch execution.

| Field | Type |
|---|---|
| AnalyticalMethod | string |
| MeasurementFrequency | FlexibleQuantityType |
| Duration | DurationType |
| Equipment | string |

## IPC
In-Process Control — discrete sampling and off-line measurement.

| Field | Type |
|---|---|
| TestMethod | string |
| Sample | string |
| Specification | string |
| Equipment | string |

---

# Formulation Operations

## RollerCompactor
Dry granulation by roll compaction.

| Field | Type |
|---|---|
| FeedMaterial | string |
| RollPressure | FlexibleQuantityType |
| RollSpeed | FlexibleQuantityType |
| GapWidth | FlexibleQuantityType |
| GranuleSize | FlexibleQuantityType |
| Equipment | string |

## Coating
Application of a coating layer to particles or tablets.

| Field | Type |
|---|---|
| CoreMaterial | string |
| CoatingMaterial | string |
| CoatingMethod | string |
| SprayRate | FlexibleQuantityType |
| Temperature | TemperatureType |
| Duration | DurationType |
| Equipment | string |

## FluidBedGranulator
Granulation using a fluidised bed.

| Field | Type |
|---|---|
| FeedMaterial | string |
| BinderSolution | string |
| AirFlowRate | FlexibleQuantityType |
| InletTemperature | TemperatureType |
| SprayRate | FlexibleQuantityType |
| Duration | DurationType |
| GranuleSize | FlexibleQuantityType |
| Equipment | string |

---

# Elementary Operations

## EmptyOperation
No-op placeholder. Used for structural purposes.

| Field | Type |
|---|---|
| Description | string |

## GenericActor
Generic actuator command.

| Field | Type |
|---|---|
| DeviceId | string |
| Command | string |
| Parameters | string |
| Duration | DurationType |

## GenericSensor
Generic sensor reading.

| Field | Type |
|---|---|
| DeviceId | string |
| SensorType | string |
| MeasurementInterval | DurationType |
| Duration | DurationType |

## ManualInput
Prompt for human input during execution.

| Field | Type |
|---|---|
| Prompt | string |
| InputType | string |
| DefaultValue | string |
| Timeout | DurationType |

## EventRecorder
Record a process event.

| Field | Type |
|---|---|
| EventType | string |
| Description | string |
| Timestamp | string |

## SingleSpectrum
Single spectrum acquisition.

| Field | Type |
|---|---|
| Instrument | string |
| WavelengthRange | string |
| IntegrationTime | DurationType |
| Averages | integer |
