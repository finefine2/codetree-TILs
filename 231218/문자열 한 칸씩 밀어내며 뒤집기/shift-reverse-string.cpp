#include <iostream>
#include <string>

using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.

    string str, str2;
    int n, q;
    cin >> str >> n;

    for (int i = 0; i<n; i++){
        cin >> q;

        if (q == 1){
            str = str.substr(1, str.length()) + str.substr(0, 1);
            cout << str << endl;
        }
        else if (q == 2){
            str = str.substr(str.length()-1, str.length()) + str.substr(0, str.length()-1);
            cout << str << endl;
        }
        else{
            for (int i = str.length() -1; i>-1; i--){
                str2 += str[i];
            }
            str = str2;
            cout << str << endl;
        }
    }
    return 0;
}