using System;
class Blackjack {
    static void Main() {
        var mc = new double[10]; var td = new double[10]; var random = new Random(7);
        for (var i = 0; i < 500; i++) {
            var state = random.Next(10); var result = state >= 5 ? 1 : -1;
            mc[state] += .1 * (result - mc[state]); td[state] += .1 * (result - td[state]);
        }
        Console.WriteLine(string.Join(", ", mc));
    }
}
