# [3] Events, TimeSeries, and Observations

The event dimension captures post-experiment data. While the recipe (dimension 2) describes *what to do*, events describe *what happened*.

## Concepts

| Concept | Description |
|---|---|
| **Event** | A discrete occurrence during batch execution (e.g., "target temperature reached") |
| **Eventframe** | An event with explicit start and end timestamps — captures duration |
| **TimeSeries** | Continuous recorded variable over time (e.g., temperature log) |

## Event

A single timestamped occurrence:

```xml
<event:event xmlns:event="http://www.example.org/event">
    <event:id>1</event:id>
    <event:description>Target temperature reached</event:description>
    <event:timestamp>2023-08-08T12:34:56Z</event:timestamp>
</event:event>
```

## TimeSeries

Extends event to a collection of data points:

```xml
<ts:timeSeriesCollection xmlns:ts="http://www.example.org/timeseries">
    <ts:series>
        <ts:dataPoint>
            <ts:timestamp>2023-08-08T12:34:56Z</ts:timestamp>
            <ts:value>10.5</ts:value>
        </ts:dataPoint>
        <ts:dataPoint>
            <ts:timestamp>2023-08-08T12:35:00Z</ts:timestamp>
            <ts:value>10.8</ts:value>
        </ts:dataPoint>
    </ts:series>
</ts:timeSeriesCollection>
```

## Eventframe

Extends event with a duration (start + end):

```xml
<eventframe:basicEvent xmlns:eventframe="http://www.example.org/eventframe">
    <eventframe:id>1</eventframe:id>
    <eventframe:description>Heating phase</eventframe:description>
    <eventframe:startTimestamp>2023-08-08T12:34:56Z</eventframe:startTimestamp>
    <eventframe:endTimestamp>2023-08-08T14:34:56Z</eventframe:endTimestamp>
</eventframe:basicEvent>
```

## Contents

| File | Description |
|---|---|
| [Temperature/](Temperature/) | Example event recordings for temperature variables |

## References

- [Wiki: Event](https://github.com/Gressling/S88-light/wiki/Event)
- [Wiki: Eventframes](https://github.com/Gressling/S88-light/wiki/Eventframes)
- [Wiki: TimeSeries](https://github.com/Gressling/S88-light/wiki/TimeSeries)


