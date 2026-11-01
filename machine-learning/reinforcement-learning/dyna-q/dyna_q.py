import random


def train(steps=500, planning_steps=5):
    q, model = {}, {}
    for _ in range(steps):
        state, action = random.randrange(8), random.randrange(2)
        next_state, reward = random.randrange(8), random.choice([-1, 0, 1])
        q.setdefault((state, action), 0.0)
        q[(state, action)] += 0.1 * (reward + 0.95 * max(q.get((next_state, a), 0) for a in range(2)) - q[(state, action)])
        model[(state, action)] = (next_state, reward)
        for key in random.sample(list(model), min(planning_steps, len(model))):
            ns, r = model[key]
            q[key] += 0.1 * (r + 0.95 * max(q.get((ns, a), 0) for a in range(2)) - q[key])
    return q, model


if __name__ == "__main__":
    print(len(train()[1]), "model transitions learned")
