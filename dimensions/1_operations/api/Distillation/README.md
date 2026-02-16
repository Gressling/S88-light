# Distillation

## Description

Thermal separation of liquid mixtures based on differences in component volatilities.

## Example

```xml
<Distillation>
  <Mixture>Ethanol/Water (50:50 v/v)</Mixture>
  <Temperature>78.4 degC</Temperature>
  <Pressure>1 atm</Pressure>
  <HeatingRate>2 degC/min</HeatingRate>
  <CoolingRate>5 degC/min</CoolingRate>
  <RefluxRatio>3:1</RefluxRatio>
  <DistillateCollectors>3 x 250 mL round-bottom flasks</DistillateCollectors>
  <SolventSelection>Ethanol</SolventSelection>
  <Equipment>Vigreux column, 30 cm</Equipment>
  <SafetyMeasures>Boiling chips, overheat cutoff</SafetyMeasures>
</Distillation>
```

## Ontology

[S88/Processes/Heat Transfer](https://github.com/Gressling/S88-light/wiki/Distillation)