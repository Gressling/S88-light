# Crystallization

## Description

Controlled formation of a crystalline solid from a supersaturated solution by cooling, evaporation, or anti-solvent addition.

## Example

```xml
<Crystallization>
  <Compound>Acetylsalicylic acid</Compound>
  <Solvent>Ethanol</Solvent>
  <Temperature>5 degC</Temperature>
  <CoolingRate>0.5 degC/min</CoolingRate>
  <StirringSpeed>200 rpm</StirringSpeed>
  <CrystallizationTime>180 min</CrystallizationTime>
  <SeedCrystal>Aspirin polymorph I</SeedCrystal>
  <CrystalSize>150 um</CrystalSize>
  <CrystalShape>Needle</CrystalShape>
  <CrystalPurity>99.5 %</CrystalPurity>
  <Yield>85 %</Yield>
  <pH>3.5</pH>
  <Additives>None</Additives>
  <Equipment>Jacketed glass reactor</Equipment>
  <SafetyMeasures>Temperature monitoring, fume hood</SafetyMeasures>
</Crystallization>
```

## Ontology

[S88/Processes/Mass Transfer](https://github.com/Gressling/S88-light/wiki/Crystallization)