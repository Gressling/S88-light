# HeatExchange

## Description

Transfer of thermal energy between two fluid streams in counter-current or co-current flow configuration.

## Example

```xml
<HeatExchange>
  <HotFluid>Process water</HotFluid>
  <ColdFluid>Cooling water</ColdFluid>
  <InletTemperatureHot>80 °C</InletTemperatureHot>
  <InletTemperatureCold>15 °C</InletTemperatureCold>
  <OutletTemperatureHot>35 °C</OutletTemperatureHot>
  <OutletTemperatureCold>45 °C</OutletTemperatureCold>
  <FlowRateHot>5 L/min</FlowRateHot>
  <FlowRateCold>8 L/min</FlowRateCold>
  <HeatExchangerType>Shell-and-tube, counter-current</HeatExchangerType>
  <Equipment>Stainless steel shell-and-tube HX</Equipment>
  <SafetyMeasures>Pressure relief valve, temperature alarm</SafetyMeasures>
</HeatExchange>
```

## Ontology

[S88/Processes/Heat Transfer](https://github.com/Gressling/S88-light/wiki/HeatExchange)
