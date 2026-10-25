"""
Value Iteration & Policy Iteration on Gridworld MDP
Reference: https://mlhive.com/playground/machine-learning/reinforcement-learning/value-policy-iteration
"""

# RUN CONFIGURATION & PARAMETERS
GAMMA = 0.95
THETA = 1e-4
GRID_SIZE = 3
GOAL = (2, 2)
PIT = (1, 1)
VERBOSE = True

ACTIONS = ["UP", "DOWN", "LEFT", "RIGHT"]
DELTAS = {"UP": (-1, 0), "DOWN": (1, 0), "LEFT": (0, -1), "RIGHT": (0, 1)}

def transition(s: tuple[int, int], a: str):
    if s == GOAL or s == PIT:
        return [(1.0, s, 0.0)]
    dr, dc = DELTAS[a]
    nr, nc = max(0, min(GRID_SIZE - 1, s[0] + dr)), max(0, min(GRID_SIZE - 1, s[1] + dc))
    next_s = (nr, nc)
    reward = 1.0 if next_s == GOAL else (-1.0 if next_s == PIT else -0.04)
    return [(1.0, next_s, reward)]

def value_iteration():
    V = { (r, c): 0.0 for r in range(GRID_SIZE) for c in range(GRID_SIZE) }
    step = 1
    while True:
        delta = 0.0
        new_V = V.copy()
        for s in V:
            if s == GOAL or s == PIT:
                continue
            q_values = []
            for a in ACTIONS:
                q = sum(p * (r + GAMMA * V[next_s]) for p, next_s, r in transition(s, a))
                q_values.append(q)
            new_V[s] = max(q_values)
            delta = max(delta, abs(new_V[s] - V[s]))
        V = new_V
        if VERBOSE and (step % 5 == 0 or step == 1 or delta < THETA):
            print(f"Step {step:02d} | Max Delta: {delta:.6f}")
        step += 1
        if delta < THETA:
            break
    return V

def main():
    print(f"--- Value Iteration on {GRID_SIZE}x{GRID_SIZE} Gridworld ---")
    print(f"Gamma: {GAMMA}, Convergence Theta: {THETA}\n")
    V = value_iteration()

    print("\nFinal State-Value Grid V(s):")
    for r in range(GRID_SIZE):
        row = [f"{V[(r, c)]:+6.2f}" for c in range(GRID_SIZE)]
        print("  " + " | ".join(row))

if __name__ == "__main__":
    main()
