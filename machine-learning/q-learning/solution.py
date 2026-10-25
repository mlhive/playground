"""
Q-Learning Gridworld Environment & Agent
Reference: https://mlhive.com/playground/machine-learning/q-learning
"""

import random

# RUN CONFIGURATION & PARAMETERS
ALPHA = 0.2     # Learning rate
GAMMA = 0.9     # Discount factor
EPSILON = 0.2   # Exploration rate
EPISODES = 150  # Training episodes
GRID_SIZE = 4
START = (0, 0)
GOAL = (3, 3)
OBSTACLES = [(1, 1), (2, 2)]
TRAPS = [(1, 3)]
VERBOSE = True

ACTIONS = ["UP", "DOWN", "LEFT", "RIGHT"]
DELTAS = {
    "UP": (-1, 0),
    "DOWN": (1, 0),
    "LEFT": (0, -1),
    "RIGHT": (0, 1)
}

def step(state: tuple[int, int], action: str):
    dr, dc = DELTAS[action]
    next_s = (state[0] + dr, state[1] + dc)
    
    # Boundary and obstacle check
    if not (0 <= next_s[0] < GRID_SIZE and 0 <= next_s[1] < GRID_SIZE) or next_s in OBSTACLES:
        return state, -1.0, False  # Bump penalty
        
    if next_s == GOAL:
        return next_s, 10.0, True  # Goal reward
        
    if next_s in TRAPS:
        return next_s, -10.0, True # Trap penalty
        
    return next_s, -0.1, False    # Step cost

def train_q_learning():
    random.seed(42)
    # Initialize Q-table: Q[state][action] = 0.0
    Q = {
        (r, c): {a: 0.0 for a in ACTIONS}
        for r in range(GRID_SIZE)
        for c in range(GRID_SIZE)
    }

    for ep in range(1, EPISODES + 1):
        state = START
        done = False
        steps = 0
        total_reward = 0.0

        while not done and steps < 50:
            steps += 1
            # Epsilon-greedy action selection
            if random.random() < EPSILON:
                action = random.choice(ACTIONS)
            else:
                best_q = max(Q[state].values())
                best_actions = [a for a, q in Q[state].items() if q == best_q]
                action = random.choice(best_actions)

            next_state, reward, done = step(state, action)
            total_reward += reward

            # Q-learning update
            max_future_q = max(Q[next_state].values()) if not done else 0.0
            td_target = reward + GAMMA * max_future_q
            Q[state][action] += ALPHA * (td_target - Q[state][action])

            state = next_state

        if VERBOSE and (ep % 30 == 0 or ep == EPISODES):
            print(f"Episode {ep:03d} | Steps: {steps:02d} | Reward: {total_reward:+6.1f}")

    return Q

def print_optimal_policy(Q):
    arrow = {"UP": "^", "DOWN": "v", "LEFT": "<", "RIGHT": ">"}
    print("\nLearned Optimal Policy Grid:")
    for r in range(GRID_SIZE):
        row_str = []
        for c in range(GRID_SIZE):
            s = (r, c)
            if s == GOAL:
                row_str.append(" G ")
            elif s in OBSTACLES:
                row_str.append(" X ")
            elif s in TRAPS:
                row_str.append(" T ")
            else:
                best_a = max(Q[s], key=Q[s].get)
                row_str.append(f" {arrow[best_a]} ")
        print("".join(row_str))

def main():
    print(f"--- Q-Learning Gridworld ({GRID_SIZE}x{GRID_SIZE}) ---")
    print(f"Alpha: {ALPHA}, Gamma: {GAMMA}, Epsilon: {EPSILON}\n")
    Q = train_q_learning()
    print_optimal_policy(Q)

if __name__ == "__main__":
    main()
