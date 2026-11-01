#include <iostream>
#include <map>
#include <array>
#include <cstdlib>
int main() {
  std::map<int, std::array<double, 2>> q;
  for (int step = 0; step < 2000; ++step) {
    int state = std::rand() % 36, next = std::rand() % 36, action = std::rand() % 2;
    double reward = next / 6 == 2 || next / 6 == 3 ? 1 : -1;
    q[state][action] += .1 * (reward + .99 * std::max(q[next][0], q[next][1]) - q[state][action]);
  }
  std::cout << q.size() << " discrete states learned\n";
}
