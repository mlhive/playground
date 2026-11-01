function run(rounds = 1000, epsilon = 0.1) {
  const means = [0.2, 0.5, 0.8], estimates = [0, 0, 0], counts = [0, 0, 0];
  for (let i = 0; i < rounds; i++) {
    const best = estimates.indexOf(Math.max(...estimates));
    const arm = Math.random() < epsilon ? Math.floor(Math.random() * 3) : best;
    const reward = Math.random() < means[arm] ? 1 : 0;
    counts[arm]++;
    estimates[arm] += (reward - estimates[arm]) / counts[arm];
  }
  return { estimates, counts };
}
console.log(run());
