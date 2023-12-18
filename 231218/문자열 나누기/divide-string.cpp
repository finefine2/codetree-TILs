#include <iostream>
#include <string>

using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.

    int n, cnt = 0, line = 0;
    string str, tmp;
    cin >> n;

    for (int i = 0; n>i; i++){
        cin >> tmp;
        str += tmp;
    }

    for (int i = 0 ; str[i] != '\0'; i++){
        if (cnt == 5){
            cout << endl;
            line++;
            cnt = 0;
        }

        cout << str[i];
        cnt ++;
    }


    return 0;
}