#include <bits/stdc++.h>
using namespace std;
 
string result(string s){
    string res = "";
    set<char> vowels = {'a','e', 'i','o','u','y'};
    for (int i = 0; i < s.size(); i++){
        if(vowels.count(tolower((unsigned char)s[i])) == 0){
            res+= ".";
            res+= tolower((unsigned char)s[i]);
        }
    }
    return res;
}

int main(){
    string phrase;
    cin >> phrase;
    cout << result(phrase) << endl;
}