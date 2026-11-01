function compare(episodes = 500) {
  const mc = new Map(), td = new Map();
  for (let i = 0; i < episodes; i++) {
    const total = 12 + Math.floor(Math.random() * 10), result = total >= 17 ? 1 : -1;
    for (const state of [total]) {
      mc.set(state, (mc.get(state) || 0) + .1 * (result - (mc.get(state) || 0)));
      td.set(state, (td.get(state) || 0) + .1 * (result - (td.get(state) || 0)));
    }
  }
  return { mc: Object.fromEntries(mc), td: Object.fromEntries(td) };
}
console.log(compare());
