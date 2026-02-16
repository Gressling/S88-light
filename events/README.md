# Event 
**Is the basic class**

The concept of "event" is multifaceted and its meaning can vary based on the context. In the realm of experiments, time, and observations, an "event" generally refers to a specific occurrence or happening that can be observed, measured, or recorded. Let's dive into this concept in the context you mentioned:

1. **Experiments**:
    - In an experimental setting, an "event" typically denotes a single occurrence of a particular outcome or result. For instance, in a coin toss experiment, each individual toss that results in either a head or tail is an "event".
    - Experiments often aim to calculate the probability of certain events. For example, in a dice roll, the probability of the event "rolling a 6" is 1/6.
    - An event could also refer to a specific set of outcomes. For instance, "rolling an even number" would encompass the results 2, 4, and 6.

2. **Time**:
    - In the context of time, an "event" can denote a particular instant or period when something occurs. This might be marked by a beginning and end time, or a specific moment in time.
    - For example, in the world of physics, especially in the study of relativity, the term "event" has a very specific meaning: it refers to a single point in spacetime, defined by both its location in space and its moment in time.

3. **Observations**:
    - When we observe natural phenomena or the outcomes of experiments, an "event" refers to a distinct observation or occurrence. In statistics, for instance, the set of all possible events is termed as the sample space.
    - For observational studies, an "event" might be something like the observation of a particular type of bird in a region, the occurrence of a certain type of weather pattern, or a patient showing a specific symptom in a medical study.
    
To summarize, in the context of experiments, time, and observations, an "event" refers to a specific, observable, and often measurable occurrence. The exact nature of that occurrence can vary widely depending on the subject matter and the context in which the term is being used.

## Time series 
**extends event to a specific type of collection**

```xml
<?xml version="1.0"?>
<event:root xmlns:event="http://www.example.org/event" xmlns:ts="http://www.example.org/timeseries">
    <event:event>
        <event:id>1</event:id>
        <event:description>Sample Event Description</event:description>
        <event:timestamp>2023-08-08T12:34:56Z</event:timestamp>
        
        <!-- Time Series Collection -->
        <ts:timeSeriesCollection>
            <ts:series>
                <ts:dataPoint>
                    <ts:timestamp>2023-08-08T12:34:56Z</ts:timestamp>
                    <ts:value>10.5</ts:value>
                </ts:dataPoint>
                <ts:dataPoint>
                    <ts:timestamp>2023-08-08T12:35:00Z</ts:timestamp>
                    <ts:value>10.8</ts:value>
                </ts:dataPoint>
                <!-- ... more data points ... -->
            </ts:series>
            <!-- ... more series ... -->
        </ts:timeSeriesCollection>
    </event:event>
</event:root>
```

Here, we've:

1. Defined two namespaces:
   - `event`: Represents the basic class of an event.
   - `ts`: Represents the time series data related to an event.
   
2. Used the `event` namespace to define attributes of a basic event, such as its `id`, `description`, and a single `timestamp`.

3. Used the `ts` namespace to define a collection of time series data. Within this collection, we can have multiple series of data, and each series can have multiple data points with a timestamp and a value.

## Event frame 
**extends event with a duration**

Certainly. In the context of 'Event Frames', the concept emphasizes the duration of an event or observation, capturing both the start and end times. Here's how we might define an XML namespace to express this:

```xml
<?xml version="1.0"?>
<event:root xmlns:event="http://www.example.org/event" xmlns:eventframe="http://www.example.org/eventframe">
    <eventframe:basicEvent>
        <eventframe:id>1</eventframe:id>
        <eventframe:description>Sample Basic Event Description</eventframe:description>
        <eventframe:startTimestamp>2023-08-08T12:34:56Z</eventframe:startTimestamp>
        <eventframe:endTimestamp>2023-08-08T14:34:56Z</eventframe:endTimestamp>
    </eventframe:basicEvent>
</event:root>
```

Here's a breakdown of the XML:

1. **Namespaces**:
   - `event`: Represents the basic class of an event.
   - `frame`: Represents the concept of 'Event Frames', focusing on the duration.

2. **Basic Event**:
   - Uses the `event` namespace to define basic attributes of an event like its `id`, `description`, and a single `timestamp`.

3. **Eventframe**:
   - Uses the `eventframe` namespace to express the extended concept of 'Event Frames'.
   - Instead of just a single timestamp, an 'Event Frame' captures both the start (`startTimestamp`) and end (`endTimestamp`) of the observation, highlighting its duration.


