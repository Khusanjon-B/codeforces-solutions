#include <bits/stdc++.h>
using namespace std;

int main() {
    string s;
    string r;
    cin >> s;
    int onlyUpper = 0;
    int onlyFirst = 0;
    for (int i = 0; i < s.size(); i++) {
        if (isupper(s[i])) {
            onlyUpper++;
            if (i != 0){
                onlyFirst++;
            
        } else {
            if(i == 0) {
                onlyFirst++;
            }
        }
    }
    if (onlyFirst == s.size() || onlyUpper == s.size()){
        for (int i = 0; i < s.size(); i++) {
            if(isupper(s[i])){
                r += tolower(s[i]);
            } else {
                r += toupper(s[i]);
            }
        }
        cout << r << endl;
        return 0;
    }
    cout << s << endl;
}