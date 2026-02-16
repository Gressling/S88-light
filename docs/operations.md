# Unit Operation Reference

24 operations are defined. For each, **bold** fields are required; all others are optional. Every operation accepts an optional `SafetyMeasures` (string) unless noted otherwise.

---

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
