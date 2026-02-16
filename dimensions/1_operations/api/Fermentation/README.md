# Fermentation

## Description

Microbial or enzymatic biotransformation of substrates into desired products under controlled conditions.

## Example

```xml
<Fermentation>
  <MicroorganismStrain>Saccharomyces cerevisiae ATCC 9763</MicroorganismStrain>
  <InoculumSize>5 %v/v</InoculumSize>
  <Feedstock>Glucose (20 g/L)</Feedstock>
  <NutrientComposition>YPD medium</NutrientComposition>
  <pH>5.0</pH>
  <Temperature>30 degC</Temperature>
  <AerationOrOxygenation>1.0 vvm</AerationOrOxygenation>
  <FermentationTime>48 h</FermentationTime>
  <AgitationOrMixing>250 rpm</AgitationOrMixing>
  <FermentationVesselType>Stirred-tank bioreactor, 5 L</FermentationVesselType>
  <ProductRecovery>Centrifugation + distillation</ProductRecovery>
  <YieldAndProductivity>0.45 g/g glucose</YieldAndProductivity>
  <SafetyMeasures>Sterile technique, BSL-1</SafetyMeasures>
</Fermentation>
```

## Ontology

[S88/Processes/Mass Transfer](https://github.com/Gressling/S88-light/wiki/Fermentation)