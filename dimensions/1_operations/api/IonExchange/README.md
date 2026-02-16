# IonExchange

## Description

Reversible exchange of ions between a feed solution and a solid ion-exchange resin for purification or separation.

## Example

```xml
<IonExchange>
  <IonExchangeResinType>Strong cation (sulfonated polystyrene)</IonExchangeResinType>
  <IonExchangeCapacity>2.0 meq/mL</IonExchangeCapacity>
  <FeedSolution>Hard water (Ca2+ 120 mg/L)</FeedSolution>
  <ContactTime>30 min</ContactTime>
  <Temperature>25 degC</Temperature>
  <FlowRate>2 BV/h</FlowRate>
  <RegenerationMethod>10 % NaCl solution</RegenerationMethod>
  <pH>7.0</pH>
  <Equipment>Glass column, 2.5 x 30 cm</Equipment>
  <SafetyMeasures>Chemical-resistant gloves</SafetyMeasures>
</IonExchange>
```

## Ontology

[S88/Processes/Mass Transfer](https://github.com/Gressling/S88-light/wiki/IonExchange)