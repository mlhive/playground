#include <algorithm>
#include <array>
#include <cstdlib>
#include <iostream>

int main() {
  std::array<std::array<double, 4>, 16> q{};
  const int moves[4][2] = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
  for (int episode = 0; episode < 500; ++episode) {
    int state = 0;
    for (int step = 0; step < 100 && state != 15; ++step) {
      int action = std::rand() % 4;
      if (std::rand() % 10 != 0) action = std::max_element(q[state].begin(), q[state].end()) - q[state].begin();
      int row = state / 4, col = state % 4;
      int nr = std::max(0, std::min(3, row + moves[action][0]));
      int nc = std::max(0, std::min(3, col + moves[action][1]));
      int next = nr * 4 + nc;
      double reward = next == 15 ? 1.0 : -0.02;
      double best = *std::max_element(q[next].begin(), q[next].end());
      q[state][action] += 0.2 * (reward + (next == 15 ? 0 : 0.95 * best) - q[state][action]);
      state = next;
    }
  }
  for (const auto& row : q) std::cout << *std::max_element(row.begin(), row.end()) << ' ';
}
