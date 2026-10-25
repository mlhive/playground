# Q-Learning Gridworld Visualizer

[![Interactive Visualizer](https://img.shields.io/badge/MLHive-Live_Playground-blue?style=for-the-badge)](https://mlhive.com/playground/machine-learning/q-learning)

Interactive visualizer reference: [https://mlhive.com/playground/machine-learning/q-learning](https://mlhive.com/playground/machine-learning/q-learning)

![Q-Learning Preview](https://mlhive.com/playground/ml-models.png)

---

## Overview

Q-Learning is a model-free reinforcement learning algorithm where an agent learns the value of state-action pairs $Q(s, a)$ to navigate an environment toward high-reward goal states while avoiding hazards.

### Bellman Optimality Q-Update:

$$Q(s, a) \leftarrow Q(s, a) + \alpha \left[ r + \gamma \max_{a'} Q(s', a') - Q(s, a) \right]$$

- $\alpha$: Learning Rate (speed of convergence)
- $\gamma$: Discount Factor (weight of future rewards)
- $\epsilon$: Exploration rate ($epsilon$-greedy policy)

---

## Visualizer Parameters & Run Configuration

Parameters matching the visualizer controls at [MLHive](https://mlhive.com/playground/machine-learning/q-learning):

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `ALPHA` | `float` | `0.2` | Learning rate |
| `GAMMA` | `float` | `0.9` | Future reward discount factor |
| `EPSILON` | `float` | `0.2` | Exploration probability |
| `EPISODES` | `int` | `150` | Number of training episodes |
| `GRID_SIZE` | `int` | `4` | 4x4 Grid dimensions |

---

## Implementations

- **Python**: [`solution.py`](./solution.py)

### How to Run

```bash
python solution.py
```
