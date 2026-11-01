function train(steps = 500, planningSteps = 5) {
  const q = new Map(), model = new Map(), value = (s, a) => q.get(`${s}:${a}`) || 0;
  for (let i = 0; i < steps; i++) {
    const state = Math.floor(Math.random() * 8), action = Math.floor(Math.random() * 2);
    const next = Math.floor(Math.random() * 8), reward = [-1, 0, 1][Math.floor(Math.random() * 3)];
    const key = `${state}:${action}`;
    q.set(key, value(state, action) + .1 * (reward + .95 * Math.max(value(next, 0), value(next, 1)) - value(state, action)));
    model.set(key, [next, reward]);
    for (const sampled of [...model.keys()].sort(() => Math.random() - .5).slice(0, planningSteps)) {
      const [ns, r] = model.get(sampled), [s, a] = sampled.split(":").map(Number);
      q.set(sampled, value(s, a) + .1 * (r + .95 * Math.max(value(ns, 0), value(ns, 1)) - value(s, a)));
    }
  }
  return model.size;
}
console.log(`${train()} model transitions learned`);
