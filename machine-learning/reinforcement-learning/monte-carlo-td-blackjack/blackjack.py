import random


def episode():
    total = random.randint(12, 21)
    return [(total, 0), (total, 1)], 1 if total >= 17 else -1


def compare(episodes=500):
    mc, td = {}, {}
    for _ in range(episodes):
        states, result = episode()
        returns = result
        for state, _ in reversed(states):
            mc[state] = mc.get(state, 0) + 0.1 * (returns - mc.get(state, 0))
            td[state] = td.get(state, 0) + 0.1 * (result - td.get(state, 0))
            returns = result
    return mc, td


if __name__ == "__main__":
    print(compare())
