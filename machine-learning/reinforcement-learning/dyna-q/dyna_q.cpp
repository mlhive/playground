#include <iostream>
#include <map>
#include <cstdlib>
#include <algorithm>
int main() {
  std::map<std::pair<int, int>, std::pair<int, double>> model;
  std::map<std::pair<int, int>, double> q;
  for (int i = 0; i < 500; ++i) {
    int s = std::rand() % 8, a = std::rand() % 2, ns = std::rand() % 8; double r = std::rand() % 3 - 1;
    auto key = std::make_pair(s, a); q[key] += .1 * (r + .95 * std::max(q[{ns, 0}], q[{ns, 1}]) - q[key]);
    model[key] = {ns, r};
    int count = 0; for (const auto& [sample, result] : model) { if (count++ == 5) break; q[sample] += .1 * (result.second + .95 * std::max(q[{result.first, 0}], q[{result.first, 1}]) - q[sample]); }
  }
  std::cout << model.size() << " model transitions learned\n";
}
