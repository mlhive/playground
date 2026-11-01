import random
from collections import deque


def train(steps=2000):
    q, memory = {}, deque(maxlen=500)
    for step in range(steps):
        state = (random.randrange(6), random.randrange(6))
        action = random.randrange(2)
        next_state = (max(0, min(5, state[0] + random.choice([-1, 0, 1])),), max(0, min(5, state[1] + random.choice([-1, 0, 1]))))
        reward = 1.0 if next_state[0] in (2, 3) else -1.0
        memory.append((state, action, reward, next_state))
        if len(memory) > 32:
            for s, a, r, ns in random.sample(memory, 32):
                q.setdefault(s, [0.0, 0.0]); q.setdefault(ns, [0.0, 0.0])
                q[s][a] += 0.1 * (r + 0.99 * max(q[ns]) - q[s][a])
    return q


if __name__ == "__main__":
    print(len(train()), "discrete states learned")
