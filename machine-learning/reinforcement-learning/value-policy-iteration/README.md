<<<<<<< HEAD
# Value & Policy Iteration

Dynamic-programming planning algorithms for a known gridworld model.

Live visualizer: https://mlhive.com/playground/machine-learning/reinforcement-learning/value-policy-iteration

Implementations: [Python](./value_policy_iteration.py), [JavaScript](./value_policy_iteration.js), [C++](./value_policy_iteration.cpp), [Rust](./value_policy_iteration.rs), [C#](./ValuePolicyIteration.cs).
=======
# Value & Policy Iteration Visualizer

[![Interactive Visualizer](https://img.shields.io/badge/MLHive-Live_Playground-blue?style=for-the-badge)](https://mlhive.com/playground/machine-learning/reinforcement-learning/value-policy-iteration)

Interactive visualizer reference: [https://mlhive.com/playground/machine-learning/reinforcement-learning/value-policy-iteration](https://mlhive.com/playground/machine-learning/reinforcement-learning/value-policy-iteration)

![Value & Policy Iteration Preview](https://mlhive.com/playground/ml-models.png)

---

## Overview

Value Iteration and Policy Iteration are foundational dynamic programming algorithms for Markov Decision Processes (MDPs) with known transition models.

### Bellman Equations

- **Value Iteration**:
  $$V_{k+1}(s) = \max_{a} \sum_{s'} P(s'|s, a) [R(s, a, s') + \gamma V_k(s')]$$

- **Policy Evaluation**:
  $$V^\pi(s) = \sum_{s'} P(s'|s, \pi(s)) [R(s, \pi(s), s') + \gamma V^\pi(s')]$$

- **Policy Improvement**:
  $$\pi_{new}(s) = \arg\max_a \sum_{s'} P(s'|s, a) [R(s, a, s') + \gamma V^\pi(s')]$$

---

## Visualizer Parameters & Run Configuration

Parameters matching the visualizer controls at [MLHive](https://mlhive.com/playground/machine-learning/reinforcement-learning/value-policy-iteration):

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `GAMMA` | `float` | `0.95` | Discount factor |
| `THETA` | `float` | `1e-4` | Convergence threshold for Bellman error |
| `ALGORITHM` | `string` | `"value_iteration"` | Technique (`"value_iteration"`, `"policy_iteration"`) |

---

## Implementations

- **Python**: [`solution.py`](./solution.py)

### How to Run

```bash
python solution.py
```
>>>>>>> 85628891dcfbd1e4fd30e0433104bea85a5cc2f2
