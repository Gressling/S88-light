# Mixing

## Description

Combining two or more ingredients into a homogeneous mixture by mechanical or diffusive means.

## Example

```xml
<Mixing>
  <Ingredients>
    <Ingredient>
      <Name>Sodium hydroxide</Name>
      <Quantity>50 mL (2 M)</Quantity>
    </Ingredient>
    <Ingredient>
      <Name>Acetic anhydride</Name>
      <Quantity>25 mL</Quantity>
    </Ingredient>
  </Ingredients>
  <MixingMethod>Magnetic stirring</MixingMethod>
  <MixingTime>10 min</MixingTime>
  <MixingTemperature>25 degC</MixingTemperature>
  <MixingSpeed>400 rpm</MixingSpeed>
  <MixingContainer>Erlenmeyer flask, 250 mL</MixingContainer>
  <InertAtmosphere>N2</InertAtmosphere>
  <PostMixingTreatment>None</PostMixingTreatment>
  <HomogeneityTesting>Visual inspection</HomogeneityTesting>
  <SafetyMeasures>Fume hood, splash guard</SafetyMeasures>
</Mixing>
```

## Ontology

[S88/Processes/Mass Transfer](https://github.com/Gressling/S88-light/wiki/Mixing)