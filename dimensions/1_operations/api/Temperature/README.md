# Temperature

## Description

Controlled heating or cooling of a process stream or vessel to reach and maintain a defined temperature setpoint.

## Example

```xml
<Temperature>
  <TargetTemperature>70 degC</TargetTemperature>
  <Duration>30 min</Duration>
  <HeatingRate>2 degC/min</HeatingRate>
  <CoolingRate>1 degC/min</CoolingRate>
  <Equipment>Jacketed reactor with thermostat</Equipment>
  <SafetyMeasures>Over-temperature cutoff</SafetyMeasures>
</Temperature>
```

## Ontology

[S88/Processes/Heat Transfer](https://github.com/Gressling/S88-light/wiki/Temperature)