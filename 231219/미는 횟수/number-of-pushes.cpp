#include <iostream>
#include <string>

using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    string a, b;

    cin >> a >> b;

    int n = 0;
    int len = a.length();

    for (int i = 0; i < len+2; i++){
        if (i == len+1){
            cout << -1;
            break;
        }
        a = a.substr(len-1, 1) + a.substr(0, len-1);
        if (a == b){
            cout << i+1;
            break;
        }
        
    }
    // abcdef
    // fabcde
    // efabcd
    // defabc
    // cdefab
    // bcdefa
    // abcdef
    

    return 0;
}