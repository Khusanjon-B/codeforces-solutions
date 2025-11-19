#include <iostream>
using namespace std;
int main(){
    int n;
    cin >> n;
    int xsum = 0;
    int ysum = 0;
    int zsum = 0;
    for (int i = 0; i < n; i++){
        int x, y, z;
        cin >> x >> y >> z;
        xsum += x;
        ysum += y;
        zsum += z;
        //cout << xsum << " " << ysum << " " << zsum << endl;
    }
    if (xsum == 0 && ysum == 0 && zsum == 0) {
        cout << "YES" << endl;
    } else {
        cout << "NO" << endl;
    }
}