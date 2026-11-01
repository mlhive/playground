def value_iteration(size=4, gamma=0.95, sweeps=50):
    values = [0.0] * (size * size)
    for _ in range(sweeps):
        updated = values[:]
        for state in range(size * size - 1):
            row, col = divmod(state, size)
            neighbors = [max(0, min(size - 1, row + dr)) * size + max(0, min(size - 1, col + dc))
                         for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]]
            updated[state] = -0.02 + gamma * max(values[n] for n in neighbors)
        values = updated
    return values


if __name__ == "__main__":
    print([round(v, 3) for v in value_iteration()])
