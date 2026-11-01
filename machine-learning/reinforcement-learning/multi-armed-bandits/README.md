<<<<<<< HEAD
# Multi-Armed Bandits

Epsilon-greedy action selection balances exploration and exploitation.

Live visualizer: https://mlhive.com/playground/machine-learning/reinforcement-learning/multi-armed-bandits

Implementations: [Python](./multi_armed_bandits.py), [JavaScript](./multi_armed_bandits.js), [C++](./multi_armed_bandits.cpp), [Rust](./multi_armed_bandits.rs), [C#](./MultiArmedBandits.cs).
=======
# Multi-Armed Bandit Arena Visualizer

[![Interactive Visualizer](https://img.shields.io/badge/MLHive-Live_Playground-blue?style=for-the-badge)](https://mlhive.com/playground/machine-learning/reinforcement-learning/multi-armed-bandits)

Interactive visualizer reference: [https://mlhive.com/playground/machine-learning/reinforcement-learning/multi-armed-bandits](https://mlhive.com/playground/machine-learning/reinforcement-learning/multi-armed-bandits)

![Bandit Arena Preview](https://mlhive.com/playground/ml-models.png)

---

## Overview

The Multi-Armed Bandit problem explores the fundamental trade-off between exploration and exploitation. A gambler faces $K$ slot machines with unknown probability distributions.

### Implemented Strategies:
1. **$epsilon$-Greedy**: Explores random arm with probability $epsilon$, otherwise picks best empirical arm.
2. **Upper Confidence Bound (UCB1)**:
   $$A_t = \arg\max_a \left[ Q(a) + c \sqrt{\frac{\ln t}{N_t(a)}} \right]$$
3. **Thompson Sampling**: Beta posterior probability sampling.

---

## Visualizer Parameters & Run Configuration

Parameters matching the visualizer controls at [MLHive](https://mlhive.com/playground/machine-learning/reinforcement-learning/multi-armed-bandits):

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `ROUNDS` | `int` | `1000` | Total time horizon / number of pulls |
| `EPSILON` | `float` | `0.1` | Exploration rate for $epsilon$-Greedy |
| `UCB_C` | `float` | `2.0` | Exploration bonus coefficient for UCB1 |

---

## Implementations

- **Python**: [`solution.py`](./solution.py)

### How to Run

```bash
python solution.py
```
>>>>>>> 85628891dcfbd1e4fd30e0433104bea85a5cc2f2
