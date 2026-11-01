function train(episodes = 500, alpha = 0.2, gamma = 0.95, epsilon = 0.1) {
  const q = Array.from({ length: 16 }, () => [0, 0, 0, 0]);
  const moves = [[-1, 0], [1, 0], [0, -1], [0, 1]];
  for (let episode = 0; episode < episodes; episode++) {
    let state = 0;
    for (let step = 0; step < 100 && state !== 15; step++) {
      const [row, col] = [Math.floor(state / 4), state % 4];
      const action = Math.random() < epsilon ? Math.floor(Math.random() * 4) : q[state].indexOf(Math.max(...q[state]));
      const [dr, dc] = moves[action];
      const nextState = Math.min(3, Math.max(0, row + dr)) * 4 + Math.min(3, Math.max(0, col + dc));
      const reward = nextState === 15 ? 1 : -0.02;
      const target = nextState === 15 ? reward : reward + gamma * Math.max(...q[nextState]);
      q[state][action] += alpha * (target - q[state][action]);
      state = nextState;
    }
  }
  return q;
}
console.log(train().map(row => Math.max(...row).toFixed(2)));
