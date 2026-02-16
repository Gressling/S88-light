# [2] Sequence — Workflow and Recipe

The sequence dimension defines the order in which unit operations execute. A `<Recipe>` contains a `<Sequence>` of steps that run serially, with optional `<Parallel>` and `<Loop>` constructs for concurrent and iterative execution.

See the [unified schema](../../s88-light.xsd) for the formal definition and the [specification](../../docs/specification.md) for orchestration semantics.

> **Note:** The legacy `Sequences.xsd` used `<Sequences>` (plural) as root.
> The unified schema uses `<Recipe>` → `<Sequence>`.

## Example (unified schema)

~~~ xml
<Recipe xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        xsi:noNamespaceSchemaLocation="../../s88-light.xsd">
  <Sequence>

    <!-- Step 0: runs first -->
    <Setup>
      <ExperimentName>Example</ExperimentName>
    </Setup>

    <!-- Steps 1-2: loop with break condition -->
    <Loop>
      <Iterations>10</Iterations>
      <BreakCondition>temperature &gt; 70</BreakCondition>
      <Body>
        <Stirring>
          <StirringSpeed unit="RPM">500</StirringSpeed>
        </Stirring>
        <Temperature name="heat">
          <TargetTemperature unit="°C">60</TargetTemperature>
        </Temperature>
      </Body>
    </Loop>

    <!-- Steps 3a + 3b: parallel execution -->
    <Parallel>
      <AddOnce>
        <Chemical>
          <Name>Reagent A</Name>
          <Amount unit="ml">10</Amount>
        </Chemical>
      </AddOnce>
      <AddOnce>
        <Chemical>
          <Name>Reagent B</Name>
          <Amount unit="g">5</Amount>
        </Chemical>
      </AddOnce>
    </Parallel>

    <!-- Step 4: final -->
    <Filtration>
      <FilterType>Vacuum</FilterType>
    </Filtration>

  </Sequence>
</Recipe>
~~~
![image](https://github.com/Gressling/S88-NG/assets/21124662/97d4b405-8fdb-430e-aa9e-0c59ebf306a9)


### PlantUML
~~~ uml
@startuml
start
  :UnitOperation0;
  fork
    :UnitOperation1;
    :UnitOperation2;
    fork again
    fork
      :UnitOperation3a;
      fork again
        :UnitOperation3b;
      end fork
    end fork
    :UnitOperation4;
end
@enduml
~~~
