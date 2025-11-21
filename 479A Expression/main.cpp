#include <bits/stdc++.h>
using namespace std;

int main() {
    int a, b, c;
    cin >> a >> b >> c;
    vector<int> nums = {a+b+c, (a+b)*c, a*(b+c), a*b*c, a*b+c, a+b*c};
    int max = 0;
    for (int i = 0; i < nums.size(); i++){
        if (max < nums[i]) max = nums[i];
    }
    cout << max << endl;
}