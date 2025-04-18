#include <iostream>
using namespace std;
bool IsEven(int n) {
  if (n % 2 == 0) {
    return true;
  }
  return false;
}
int ThreeXPlusOneConjecture(int x) {
  if (x == 1) {
    return 1;
  }
  if (IsEven(x)) {
    return ThreeXPlusOneConjecture(x / 2);
  } else
    return ThreeXPlusOneConjecture(3 * x + 1);
}
int main() {
  int n;
  cin >> n;
  cout << ThreeXPlusOneConjecture(n);
}
