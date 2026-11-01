#include <array>
#include <algorithm>
#include <iostream>
int main() {
  std::array<double, 16> values{};
  for (int sweep = 0; sweep < 50; ++sweep) {
    auto next = values;
    for (int state = 0; state < 15; ++state) {
      int row = state / 4, col = state % 4;
      int neighbors[] = {std::max(0, row - 1) * 4 + col, std::min(3, row + 1) * 4 + col,
                         row * 4 + std::max(0, col - 1), row * 4 + std::min(3, col + 1)};
      double best = *std::max_element(neighbors, neighbors + 4, [&](int a, int b) { return values[a] < values[b]; });
      next[state] = -.02 + .95 * values[best];
    }
    values = next;
  }
  for (double value : values) std::cout << value << ' ';
}
