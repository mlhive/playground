"""
Autoregressive LLM Inference & Sampling (Temperature, Top-K, Top-P)
Reference: https://mlhive.com/playground/generative-ai/llm-inference
"""

import math
import random

# ==========================================
# RUN CONFIGURATION & PARAMETERS
# ==========================================
MODEL_NAME = "gemma3-1b"
PROMPT = "Explain how neural networks learn in simple terms:"
SYSTEM_PROMPT = "You are an expert AI educator explaining complex topics simply."
TEMPERATURE = 0.7
TOP_P = 0.9
TOP_K = 40
MAX_TOKENS = 32
REPETITION_PENALTY = 1.1
VERBOSE = True

# Mock token vocabulary and distribution for demonstration
VOCABULARY = [
    "Neural", "networks", "learn", "by", "adjusting", "their", "internal",
    "weights", "using", "gradient", "descent", "and", "backpropagation.",
    "During", "training,", "the", "model", "compares", "its", "predictions",
    "against", "ground", "truth", "targets,", "calculates", "loss,", "and",
    "updates", "parameters", "step", "step.", "gradually", "improving", "accuracy."
]

def sample_next_token(logits: list[float], temp: float, top_k: int, top_p: float):
    if temp == 0.0:
        # Greedy
        return logits.index(max(logits))

    # 1. Temperature scaling
    scaled_logits = [z / temp for z in logits]

    # 2. Softmax
    shift = max(scaled_logits)
    exps = [math.exp(z - shift) for z in scaled_logits]
    sum_exps = sum(exps)
    probs = [e / sum_exps for e in exps]

    # 3. Top-K filtering
    indexed_probs = sorted(list(enumerate(probs)), key=lambda x: -x[1])
    indexed_probs = indexed_probs[:top_k]

    # 4. Top-P (Nucleus) filtering
    cum_prob = 0.0
    nucleus = []
    for idx, p in indexed_probs:
        nucleus.append((idx, p))
        cum_prob += p
        if cum_prob >= top_p:
            break

    # Re-normalize
    norm_sum = sum(p for _, p in nucleus)
    r = random.random() * norm_sum
    current = 0.0
    for idx, p in nucleus:
        current += p
        if current >= r:
            return idx
    return nucleus[0][0]

def simulate_llm_inference(prompt: str, max_tokens: int, temp: float, top_k: int, top_p: float):
    random.seed(42)
    generated_tokens = []
    vocab_size = len(VOCABULARY)

    print(f"User Prompt: '{prompt}'")
    print(f"Streaming Output: ", end="", flush=True)

    for step in range(min(max_tokens, vocab_size)):
        # Generate pseudo-logits favoring semantic sequence
        logits = [random.gauss(0, 1) for _ in range(vocab_size)]
        # Bias towards next word in pedagogical vocabulary
        next_ideal = step % vocab_size
        logits[next_ideal] += 4.0

        token_idx = sample_next_token(logits, temp, top_k, top_p)
        token = VOCABULARY[token_idx]
        generated_tokens.append(token)
        print(token + " ", end="", flush=True)

    print("\n")
    return " ".join(generated_tokens)

def main():
    print(f"--- On-Device LLM Inference Visualizer ---")
    print(f"Model: {MODEL_NAME}")
    print(f"Temperature: {TEMPERATURE}, Top-P: {TOP_P}, Top-K: {TOP_K}, Max Tokens: {MAX_TOKENS}")
    print(f"System: {SYSTEM_PROMPT}\n")

    result = simulate_llm_inference(PROMPT, MAX_TOKENS, TEMPERATURE, TOP_K, TOP_P)
    print(f"Final Completed Generation:")
    print(f"\"{result}\"")

if __name__ == "__main__":
    main()
