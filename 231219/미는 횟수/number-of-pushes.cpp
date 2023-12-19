#include <iostream>
#include <string>

using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    string a, b;

    cin >> a >> b;

    int n = 0;
    int len = a.length();

    for (int i = 0; i < len+1; i++){
        if (i == len){
            cout << -1;
            break;
        }
        if (a == b){
            cout << i;
            break;
        }
        a = a.substr(1) + a.substr(0, 1);
        
    }
    

    return 0;
}