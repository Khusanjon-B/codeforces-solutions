#include <iostream>
#include <string>
using namespace std;
int main(){
    string word = "hello";
    char c;
    int i = 0;
    while(cin >> c){
        if (i > word.size()) continue;
        if (tolower(c) == word[i]) i++;
        //cout << "i: " << i << " c: " << c << endl;
    }
    if (i == (word.size())) cout << "YES" << endl;
    else cout << "NO" << endl;
}