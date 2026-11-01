function train(steps = 2000) {
  const q = new Map(), memory = [];
  const values = s => { if (!q.has(s)) q.set(s, [0, 0]); return q.get(s); };
  for (let step = 0; step < steps; step++) {
    const state = `${Math.floor(Math.random() * 6)},${Math.floor(Math.random() * 6)}`;
    const action = Math.floor(Math.random() * 2);
    const next = `${Math.max(0, Math.min(5, Number(state[0]) + (Math.floor(Math.random() * 3) - 1)))},${Math.floor(Math.random() * 6)}`;
    memory.push([state, action, next, next[0] === "2" || next[0] === "3" ? 1 : -1]);
    if (memory.length > 32) for (const [s, a, ns, r] of memory.slice(-32)) values(s)[a] += .1 * (r + .99 * Math.max(...values(ns)) - values(s)[a]);
  }
  return q.size;
}
console.log(`${train()} discrete states learned`);
