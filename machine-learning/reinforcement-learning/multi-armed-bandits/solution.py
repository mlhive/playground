"""
Multi-Armed Bandit Strategies (Epsilon-Greedy, UCB1, Thompson Sampling)
Reference: https://mlhive.com/playground/machine-learning/reinforcement-learning/multi-armed-bandits
"""

import math
import random

# RUN CONFIGURATION & PARAMETERS
ROUNDS = 1000
EPSILON = 0.1
UCB_C = 2.0
TRUE_PROBABILITIES = [0.10, 0.50, 0.35, 0.80, 0.25]  # Arm 3 is optimal (0.80)

def pull_arm(arm_idx: int) -> int:
    return 1 if random.random() < TRUE_PROBABILITIES[arm_idx] else 0

def run_epsilon_greedy(k: int, rounds: int, eps: float):
    counts = [0] * k
    rewards = [0] * k
    total_reward = 0

    for t in range(rounds):
        if random.random() < eps or sum(counts) == 0:
            arm = random.randint(0, k - 1)
        else:
            q_vals = [rewards[i] / counts[i] if counts[i] > 0 else 0 for i in range(k)]
            arm = q_vals.index(max(q_vals))

        r = pull_arm(arm)
        counts[arm] += 1
        rewards[arm] += r
        total_reward += r

    return total_reward, counts

def run_ucb1(k: int, rounds: int, c: float):
    counts = [0] * k
    rewards = [0] * k
    total_reward = 0

    # Initial pull of each arm
    for arm in range(k):
        r = pull_arm(arm)
        counts[arm] += 1
        rewards[arm] += r
        total_reward += r

    for t in range(k, rounds):
        ucb_values = []
        for i in range(k):
            q_mean = rewards[i] / counts[i]
            bonus = c * math.sqrt(math.log(t + 1) / counts[i])
            ucb_values.append(q_mean + bonus)
        arm = ucb_values.index(max(ucb_values))
        r = pull_arm(arm)
        counts[arm] += 1
        rewards[arm] += r
        total_reward += r

    return total_reward, counts

def run_thompson_sampling(k: int, rounds: int):
    # Beta distribution priors: alpha=1, beta=1
    alphas = [1.0] * k
    betas = [1.0] * k
    counts = [0] * k
    total_reward = 0

    for t in range(rounds):
        samples = [random.betavariate(alphas[i], betas[i]) for i in range(k)]
        arm = samples.index(max(samples))
        r = pull_arm(arm)
        counts[arm] += 1
        total_reward += r
        if r == 1:
            alphas[arm] += 1
        else:
            betas[arm] += 1

    return total_reward, counts

def main():
    random.seed(42)
    k = len(TRUE_PROBABILITIES)
    best_arm = TRUE_PROBABILITIES.index(max(TRUE_PROBABILITIES))
    print(f"--- Multi-Armed Bandit Arena ---")
    print(f"Arms: {k}, True Rewards: {TRUE_PROBABILITIES}")
    print(f"Optimal Arm: {best_arm} ({TRUE_PROBABILITIES[best_arm]*100:.0f}%)\n")

    r_eps, c_eps = run_epsilon_greedy(k, ROUNDS, EPSILON)
    r_ucb, c_ucb = run_ucb1(k, ROUNDS, UCB_C)
    r_ts, c_ts = run_thompson_sampling(k, ROUNDS)

    print(f"{'Strategy':20s} | {'Reward':6s} | {'Optimal Arm %':14s} | Arm Pulls")
    print("-" * 65)
    print(f"{'Epsilon-Greedy':20s} | {r_eps:6d} | {(c_eps[best_arm]/ROUNDS)*100:6.1f}%        | {c_eps}")
    print(f"{'UCB1':20s} | {r_ucb:6d} | {(c_ucb[best_arm]/ROUNDS)*100:6.1f}%        | {c_ucb}")
    print(f"{'Thompson Sampling':20s} | {r_ts:6d} | {(c_ts[best_arm]/ROUNDS)*100:6.1f}%        | {c_ts}")

if __name__ == "__main__":
    main()
