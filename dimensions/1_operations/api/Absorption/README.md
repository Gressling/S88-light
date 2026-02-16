# Absorption

## Description

Gas-liquid mass transfer operation in which a gaseous solute is selectively dissolved into a liquid solvent.

## Example

```xml
<Absorption>
  <GasStream>CO2</GasStream>
  <LiquidPhase>Water</LiquidPhase>
  <Solvent>Monoethanolamine (MEA)</Solvent>
  <Temperature>25 degC</Temperature>
  <Pressure>1.5 bar</Pressure>
  <MassTransferCoefficient>0.035 mol/(m2 s Pa)</MassTransferCoefficient>
  <ContactTime>120 s</ContactTime>
  <pH>9.2</pH>
  <Equipment>Packed column absorber</Equipment>
  <SafetyMeasures>Gas leak detection, ventilation</SafetyMeasures>
</Absorption>
```

## Ontology

[S88/Processes/Mass Transfer](https://github.com/Gressling/S88-light/wiki/Absorption)