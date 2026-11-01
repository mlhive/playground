#include <iostream>
#include <array>
#include <cstdlib>
int main() {
  std::array<double, 10> mc{}, td{};
  for (int i = 0; i < 500; ++i) {
    int state = std::rand() % 10, result = state >= 5 ? 1 : -1;
    mc[state] += .1 * (result - mc[state]);
    td[state] += .1 * (result - td[state]);
  }
  for (double value : mc) std::cout << value << ' ';
}
