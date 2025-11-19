#include <bits/stdc++.h>
using namespace std;
int main() {
    unsigned long long n, m, a;
    cin >> n >> m >> a;
    unsigned long long sum = ceil((1.0 * n)/a) * ceil((1.0 * m)/a);
    cout << sum << endl;
}