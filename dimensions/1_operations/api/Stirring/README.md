# Stirring

## Description

Mechanical agitation of a fluid to promote mixing, heat transfer, or mass transfer within a vessel.

## Example

```xml
<Stirring>
  <StirringSpeed>500 rpm</StirringSpeed>
  <StirringTime>60 min</StirringTime>
  <StirringDirection>Clockwise</StirringDirection>
  <StirrerDesign>Pitched-blade turbine</StirrerDesign>
  <StirrerSizeAndShape>45 mm diameter, 4-blade</StirrerSizeAndShape>
  <ContainerGeometry>Cylindrical, 1 L</ContainerGeometry>
  <MaterialOfConstruction>PTFE-coated stainless steel</MaterialOfConstruction>
  <OperationalLimits>Max 1200 rpm</OperationalLimits>
  <Viscosity>1.0 mPa s</Viscosity>
  <ShearRate>150 1/s</ShearRate>
  <AdditionalAgitationMechanisms>None</AdditionalAgitationMechanisms>
  <StirringRateProfiles>Constant</StirringRateProfiles>
  <SafetyMeasures>Splash guard, secured clamp</SafetyMeasures>
</Stirring>
```

## Ontology

[S88/Processes/Mass Transfer](https://github.com/Gressling/S88-light/wiki/Stirring)