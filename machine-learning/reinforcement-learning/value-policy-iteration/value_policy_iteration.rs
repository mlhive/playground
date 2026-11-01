fn main() {
    let mut values = [0.0_f64; 16];
    for _ in 0..50 {
        let mut next = values;
        for state in 0..15 {
            let row = state / 4; let col = state % 4;
            let ns = [row.saturating_sub(1) * 4 + col, (row + 1).min(3) * 4 + col,
                      row * 4 + col.saturating_sub(1), row * 4 + (col + 1).min(3)];
            next[state] = -.02 + .95 * ns.iter().map(|&n| values[n]).fold(f64::NEG_INFINITY, f64::max);
        }
        values = next;
    }
    println!("{:?}", values);
}
