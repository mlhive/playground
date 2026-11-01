using System;
class MultiArmedBandits {
    static void Main() {
        var means = new[] { .2, .5, .8 }; var estimates = new double[3]; var counts = new double[3]; var random = new Random(7);
        for (var i = 0; i < 1000; i++) {
            var best = Array.IndexOf(estimates, Math.Max(estimates[0], Math.Max(estimates[1], estimates[2])));
            var arm = random.NextDouble() < .1 ? random.Next(3) : best;
            var reward = random.NextDouble() < means[arm] ? 1 : 0;
            estimates[arm] += (reward - estimates[arm]) / ++counts[arm];
        }
        Console.WriteLine(string.Join(", ", estimates));
    }
}
