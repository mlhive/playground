fn main() {
    let means = [0.2, 0.5, 0.8];
    let mut estimates = [0.0; 3];
    let mut counts = [0.0; 3];
    for i in 0..1000 {
        let best = (0..3).max_by(|&a, &b| estimates[a].partial_cmp(&estimates[b]).unwrap()).unwrap();
        let arm = if i % 10 == 0 { i % 3 } else { best };
        let reward = if (i * 37 + arm * 11) % 100 < (means[arm] * 100.0) as usize { 1.0 } else { 0.0 };
        counts[arm] += 1.0;
        estimates[arm] += (reward - estimates[arm]) / counts[arm];
    }
    println!("{:?}", estimates);
}
