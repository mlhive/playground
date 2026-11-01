fn main() {
    let mut q = [[0.0_f64; 4]; 16];
    let moves = [(-1, 0), (1, 0), (0, -1), (0, 1)];
    for _ in 0..500 {
        let mut state = 0usize;
        for _ in 0..100 {
            if state == 15 { break; }
            let action = if rand_step() % 10 == 0 { rand_step() % 4 } else {
                (0..4).max_by(|&a, &b| q[state][a].partial_cmp(&q[state][b]).unwrap()).unwrap()
            };
            let row = (state / 4) as i32;
            let col = (state % 4) as i32;
            let nr = (row + moves[action].0).clamp(0, 3);
            let nc = (col + moves[action].1).clamp(0, 3);
            let next = (nr * 4 + nc) as usize;
            let reward = if next == 15 { 1.0 } else { -0.02 };
            let best = q[next].iter().copied().fold(f64::NEG_INFINITY, f64::max);
            q[state][action] += 0.2 * (reward + if next == 15 { 0.0 } else { 0.95 * best } - q[state][action]);
            state = next;
        }
    }
    println!("{:?}", q.iter().map(|r| r.iter().copied().fold(0.0, f64::max)).collect::<Vec<_>>());
}

fn rand_step() -> usize {
    use std::time::{SystemTime, UNIX_EPOCH};
    (SystemTime::now().duration_since(UNIX_EPOCH).unwrap().subsec_nanos() as usize).wrapping_mul(1664525)
}
