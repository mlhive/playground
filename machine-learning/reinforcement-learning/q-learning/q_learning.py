import random


def train(episodes=500, alpha=0.2, gamma=0.95, epsilon=0.1):
    q = [[0.0] * 4 for _ in range(16)]
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for _ in range(episodes):
        state = 0
        for _ in range(100):
            row, col = divmod(state, 4)
            action = random.randrange(4) if random.random() < epsilon else max(range(4), key=q[state].__getitem__)
            dr, dc = moves[action]
            nr, nc = max(0, min(3, row + dr)), max(0, min(3, col + dc))
            next_state = nr * 4 + nc
            reward = 1.0 if next_state == 15 else -0.02
            target = reward if next_state == 15 else reward + gamma * max(q[next_state])
            q[state][action] += alpha * (target - q[state][action])
            state = next_state
            if state == 15:
                break
    return q


if __name__ == "__main__":
    print([round(max(row), 2) for row in train()])
