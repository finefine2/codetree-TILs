#include <iostream>
#include <string>

using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    string a, b;

    cin >> a >> b;

    int n = 0;
    int len = a.length();

    if (a == b) cout << 0;
    else{

        for (int i = 1; i < len+1; i++){
            a = a.substr(1) + a.substr(0, 1);
            if (a==b){
                cout << i;
                break;
            }
        }
    }

    return 0;
}