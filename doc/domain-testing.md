# Domain Testing

## Control Flow Graph

![control flow](./control-flow.png)

## Predicates

| #              | Predicate          |
| -------------- | ------------------ |
| P<sub>1</sub>  | `gender == "boy"`  |
| P<sub>2</sub>  | `gender == "girl"` |
| P<sub>3</sub>  | `age < 6`          |
| P<sub>4a</sub> | `7 < age`          |
| P<sub>4b</sub> | `age < 10`         |
| P<sub>5a</sub> | `10 < age`         |
| P<sub>5b</sub> | `age < 15`         |
| P<sub>6</sub>  | `20 < age`         |
| P<sub>7</sub>  | `age < 6`          |
| P<sub>8a</sub> | `7 < age`          |
| P<sub>8b</sub> | `age < 10`         |
| P<sub>9a</sub> | `11 < age`         |
| P<sub>9b</sub> | `age < 15`         |
| P<sub>10</sub> | `20 < age`         |

## Domain Graph

![domain graph](./domain-graph/domain-graph.png)
