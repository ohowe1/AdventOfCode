#include <bits/stdc++.h>

#define f(i, s, k, l) for (int i = s; i < k; i += l)
#define for0(i, k) f(i, 0, k, 1)
#define nl '\n'
#define pb push_back

using namespace std;

using pi = pair<int, int>;
using vi = vector<int>;
using vvi = vector<vi>;
using ll = long long;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  int a, b;

  vector<int> aL, bL;
  while (cin >> a >> b) {
    aL.emplace_back(a);
    bL.emplace_back(b);
  }

  ranges::sort(aL);
  ranges::sort(bL);

  ll total = 0;
  for (int i = 0; i < aL.size(); i++) {
    total += abs(aL[i] - bL[i]);
  }

  cout << total << endl;
}
