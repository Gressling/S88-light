# GenericActor

## Description

Generic actuator command that sends a control instruction to a specified device.

## Example

```xml
<GenericActor>
  <DeviceId>PUMP-101</DeviceId>
  <Command>SetFlowRate</Command>
  <Parameters>25 mL/min</Parameters>
  <Duration>60 min</Duration>
</GenericActor>
```

## Ontology

[S88/Processes/Elementary](https://github.com/Gressling/S88-light/wiki/GenericActor)
