# [4] Devices — Declaration of Hardware

The device dimension optionally declares which equipment executes a unit operation. If omitted, the current device is assumed.

```xml
<Device>
    <Name>Reactor R-101</Name>
    <Type>Glass-lined stirred vessel</Type>
    <Volume unit="L">50</Volume>
    <Manufacturer>Büchi</Manufacturer>
</Device>
```

Devices are referenced from operations via the `device` attribute (e.g., `<Prepare device="R-101">`).

## References

- [Wiki: Device](https://github.com/Gressling/S88-light/wiki/Device)
