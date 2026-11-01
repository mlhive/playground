using System;
using System.Collections.Generic;
class CartPoleDqn {
    static void Main() {
        var q = new Dictionary<int, double[]>(); var random = new Random(7);
        for (var step = 0; step < 2000; step++) {
            var state = random.Next(36); var next = random.Next(36); var action = random.Next(2);
            if (!q.ContainsKey(state)) q[state] = new double[2];
            if (!q.ContainsKey(next)) q[next] = new double[2];
            var reward = next / 6 is 2 or 3 ? 1 : -1;
            q[state][action] += .1 * (reward + .99 * Math.Max(q[next][0], q[next][1]) - q[state][action]);
        }
        Console.WriteLine($"{q.Count} discrete states learned");
    }
}
