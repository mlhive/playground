using System;
using System.Collections.Generic;
class DynaQ {
    static void Main() {
        var q = new Dictionary<(int, int), double>(); var model = new Dictionary<(int, int), (int, double)>(); var random = new Random(7);
        for (var i = 0; i < 500; i++) {
            var key = (random.Next(8), random.Next(2)); var next = random.Next(8); var reward = random.Next(-1, 2);
            var current = q.GetValueOrDefault(key); q[key] = current + .1 * (reward + .95 * Math.Max(q.GetValueOrDefault((next, 0)), q.GetValueOrDefault((next, 1))) - current);
            model[key] = (next, reward);
            foreach (var sample in model.Keys) { var result = model[sample]; var old = q.GetValueOrDefault(sample); q[sample] = old + .1 * (result.Item2 + .95 * Math.Max(q.GetValueOrDefault((result.Item1, 0)), q.GetValueOrDefault((result.Item1, 1))) - old); }
        }
        Console.WriteLine($"{model.Count} model transitions learned");
    }
}
