#include <bits/stdc++.h>
using namespace std;

int main(){
    int s, n;
    cin >> s >> n;
    map<int, vector<int>> dragons;
    for (int i = 0; i < n; i++) {
        int x, y;
        cin >> x >> y;
        dragons[x].push_back(y);
    }
    int c = 0;
    for (auto d : dragons){
        if(d.first >= s) {
            cout << "NO" << endl;
            c = 1;
            break;
        } else {
            for(int i = 0; i < d.second.size(); i++){
                s += d.second[i];
            }
        }
    }
    if (c == 0) cout << "YES" << endl;
}