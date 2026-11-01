using System;

class QLearning {
    static void Main() {
        var q = new double[16, 4];
        var moves = new[] { (-1, 0), (1, 0), (0, -1), (0, 1) };
        var random = new Random(7);
        for (var episode = 0; episode < 500; episode++) {
            var state = 0;
            for (var step = 0; step < 100 && state != 15; step++) {
                var action = random.NextDouble() < .1 ? random.Next(4) : Best(q, state);
                var row = state / 4; var col = state % 4;
                var next = Math.Clamp(row + moves[action].Item1, 0, 3) * 4 + Math.Clamp(col + moves[action].Item2, 0, 3);
                var reward = next == 15 ? 1 : -.02;
                q[state, action] += .2 * (reward + (next == 15 ? 0 : .95 * BestValue(q, next)) - q[state, action]);
                state = next;
            }
        }
        for (var s = 0; s < 16; s++) Console.Write($"{BestValue(q, s):F2} ");
    }
    static int Best(double[,] q, int state) { var best = 0; for (var a = 1; a < 4; a++) if (q[state, a] > q[state, best]) best = a; return best; }
    static double BestValue(double[,] q, int state) { return q[state, Best(q, state)]; }
}
