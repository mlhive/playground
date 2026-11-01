function valueIteration(size = 4, gamma = 0.95, sweeps = 50) {
  let values = Array(size * size).fill(0);
  for (let sweep = 0; sweep < sweeps; sweep++) {
    const updated = [...values];
    for (let state = 0; state < size * size - 1; state++) {
      const row = Math.floor(state / size), col = state % size;
      const neighbors = [[-1, 0], [1, 0], [0, -1], [0, 1]].map(([dr, dc]) =>
        Math.min(size - 1, Math.max(0, row + dr)) * size + Math.min(size - 1, Math.max(0, col + dc)));
      updated[state] = -0.02 + gamma * Math.max(...neighbors.map(n => values[n]));
    }
    values = updated;
  }
  return values;
}
console.log(valueIteration().map(v => v.toFixed(3)));
