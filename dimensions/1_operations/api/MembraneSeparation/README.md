# MembraneSeparation

## Description

Pressure-driven separation process using a semi-permeable membrane to selectively permeate or reject solutes.

## Example

```xml
<MembraneSeparation>
  <MembraneType>Ultrafiltration</MembraneType>
  <MembraneMaterial>Polyethersulfone (PES)</MembraneMaterial>
  <FeedSolution>Protein solution (10 g/L BSA)</FeedSolution>
  <OperatingPressure>2 bar</OperatingPressure>
  <FeedFlowRate>500 mL/min</FeedFlowRate>
  <Temperature>25 degC</Temperature>
  <MembraneSurfaceArea>0.1 m2</MembraneSurfaceArea>
  <CleaningAndMaintenance>0.1 M NaOH CIP</CleaningAndMaintenance>
  <Equipment>Crossflow UF cassette system</Equipment>
  <SafetyMeasures>Pressure gauge, relief valve</SafetyMeasures>
</MembraneSeparation>
```

## Ontology

[S88/Processes/Mass Transfer](https://github.com/Gressling/S88-light/wiki/MembraneSeparation)