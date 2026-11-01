fn main() {
    let mut mc = [0.0_f64; 10]; let mut td = [0.0_f64; 10];
    for i in 0..500 {
        let state = i % 10; let result = if state >= 5 { 1.0 } else { -1.0 };
        mc[state] += .1 * (result - mc[state]); td[state] += .1 * (result - td[state]);
    }
    println!("MC: {:?}\nTD: {:?}", mc, td);
}
