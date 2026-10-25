# LLM Inference Playground Visualizer

[![Interactive Visualizer](https://img.shields.io/badge/MLHive-Live_Playground-blue?style=for-the-badge)](https://mlhive.com/playground/generative-ai/llm-inference)

Interactive visualizer reference: [https://mlhive.com/playground/generative-ai/llm-inference](https://mlhive.com/playground/generative-ai/llm-inference)

![Generative AI Preview](https://mlhive.com/playground/category/generative-ai-hero.webp)

---

## Overview

Simulates and executes on-device autoregressive Large Language Model (LLM) inference (e.g. Gemma 3 1B, Gemma 2 2B, SmolLM) featuring:
- Autoregressive token generation: $P(w_t \mid w_1, \dots, w_{t-1})$
- **Temperature Scaling**:
  $$P(w_i) = \frac{\exp(z_i / T)}{\sum_j \exp(z_j / T)}$$
- **Top-K Truncation**: Retains only the $K$ highest-probability logits.
- **Top-P (Nucleus) Sampling**: Retains smallest set of tokens whose cumulative probability $\ge P$.
- **Repetition Penalty**: Scales down logits of previously generated tokens to prevent degeneration.

---

## Visualizer Parameters & Run Configuration

Parameters matching the visualizer controls at [MLHive](https://mlhive.com/playground/generative-ai/llm-inference):

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `MODEL_NAME` | `string` | `"gemma3-1b"` | Model identifier (`"gemma3-1b"`, `"smollm-135m"`) |
| `TEMPERATURE` | `float` | `0.7` | Randomness scale ($0.0 = \text{greedy}, 1.0 = \text{creative}$) |
| `TOP_P` | `float` | `0.9` | Nucleus probability mass threshold |
| `TOP_K` | `int` | `40` | Maximum top candidate tokens |
| `MAX_TOKENS` | `int` | `64` | Generation length limit |
| `REPETITION_PENALTY` | `float` | `1.1` | Penalty applied to repeated tokens |

---

## Implementations

- **Python**: [`solution.py`](./solution.py)
- **JavaScript (Node.js)**: [`solution.js`](./solution.js)

### How to Run

```bash
python solution.py
node solution.js
```
