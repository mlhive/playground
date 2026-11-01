using System;
class ValuePolicyIteration {
    static void Main() {
        var values = new double[16];
        for (var sweep = 0; sweep < 50; sweep++) {
            var next = (double[])values.Clone();
            for (var state = 0; state < 15; state++) {
                var row = state / 4; var col = state % 4;
                var ns = new[] { Math.Max(0, row - 1) * 4 + col, Math.Min(3, row + 1) * 4 + col,
                    row * 4 + Math.Max(0, col - 1), row * 4 + Math.Min(3, col + 1) };
                var best = 0.0; foreach (var n in ns) best = Math.Max(best, values[n]);
                next[state] = -.02 + .95 * best;
            }
            values = next;
        }
        Console.WriteLine(string.Join(", ", values));
    }
}
