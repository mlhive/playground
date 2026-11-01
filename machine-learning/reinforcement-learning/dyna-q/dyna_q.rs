use std::collections::HashMap;
fn main() {
    let mut q: HashMap<(usize, usize), f64> = HashMap::new();
    let mut model: HashMap<(usize, usize), (usize, f64)> = HashMap::new();
    for i in 0..500 {
        let key = (i % 8, i % 2); let next = (i * 3) % 8; let reward = (i % 3) as f64 - 1.0;
        let best = q.get(&(next, 0)).copied().unwrap_or(0.0).max(q.get(&(next, 1)).copied().unwrap_or(0.0));
        *q.entry(key).or_insert(0.0) += .1 * (reward + .95 * best - q.get(&key).copied().unwrap_or(0.0));
        model.insert(key, (next, reward));
        for (&sample, &(ns, r)) in model.iter().take(5) {
            let best = q.get(&(ns, 0)).copied().unwrap_or(0.0).max(q.get(&(ns, 1)).copied().unwrap_or(0.0));
            *q.entry(sample).or_insert(0.0) += .1 * (r + .95 * best - q.get(&sample).copied().unwrap_or(0.0));
        }
    }
    println!("{} model transitions learned", model.len());
}
