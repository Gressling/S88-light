# Filtration

## Description

Solid-liquid separation by passing a suspension through a porous medium that retains the solid phase.

## Example

```xml
<Filtration>
  <FilterType>Vacuum filtration</FilterType>
  <PoreSize>0.45 um</PoreSize>
  <FeedSolution>Crystal slurry in ethanol</FeedSolution>
  <FiltrationRate>50 mL/min</FiltrationRate>
  <FilterArea>45 cm2</FilterArea>
  <FilterCakeThickness>5 mm</FilterCakeThickness>
  <FiltrationTime>20 min</FiltrationTime>
  <Temperature>20 degC</Temperature>
  <PressureOrVacuum>-200 mbar</PressureOrVacuum>
  <PreFiltrationTreatment>None</PreFiltrationTreatment>
  <CleaningAndMaintenance>Rinse with solvent</CleaningAndMaintenance>
  <FiltrationEfficiency>99.2 %</FiltrationEfficiency>
  <Equipment>Buchner funnel, PTFE membrane</Equipment>
  <SafetyMeasures>Gloves, eye protection</SafetyMeasures>
</Filtration>
```

## Ontology

[S88/Processes/Mass Transfer](https://github.com/Gressling/S88-light/wiki/Filtration)