use std::collections::HashMap;
fn main() {
    let mut q: HashMap<usize, [f64; 2]> = HashMap::new();
    for step in 0..2000 {
        let state = (step * 17) % 36; let next = (step * 29 + 3) % 36; let action = step % 2;
        let reward = if next / 6 == 2 || next / 6 == 3 { 1.0 } else { -1.0 };
        let best = q.get(&next).copied().unwrap_or([0.0, 0.0]).iter().copied().fold(0.0, f64::max);
        let entry = q.entry(state).or_insert([0.0, 0.0]);
        entry[action] += .1 * (reward + .99 * best - entry[action]);
    }
    println!("{} discrete states learned", q.len());
}
