#include <iostream>
#include <array>
#include <cstdlib>
#include <algorithm>
int main() {
  std::array<double, 3> means{.2, .5, .8}, estimates{}, counts{};
  for (int i = 0; i < 1000; ++i) {
    int arm = std::rand() % 10 == 0 ? std::rand() % 3 : std::max_element(estimates.begin(), estimates.end()) - estimates.begin();
    double reward = (std::rand() / double(RAND_MAX)) < means[arm] ? 1 : 0;
    estimates[arm] += (reward - estimates[arm]) / ++counts[arm];
  }
  for (double value : estimates) std::cout << value << ' ';
}
