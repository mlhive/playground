import random


def run(rounds=1000, epsilon=0.1):
    true_means = [0.2, 0.5, 0.8]
    estimates, counts = [0.0] * 3, [0] * 3
    for _ in range(rounds):
        arm = random.randrange(3) if random.random() < epsilon else max(range(3), key=estimates.__getitem__)
        reward = 1.0 if random.random() < true_means[arm] else 0.0
        counts[arm] += 1
        estimates[arm] += (reward - estimates[arm]) / counts[arm]
    return estimates, counts


if __name__ == "__main__":
    print(run())
