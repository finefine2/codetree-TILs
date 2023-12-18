#include <iostream>
#include <string>

using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.

    int n;
    string str, tmp;

    cin >> n;

    for (int i =0; n >i; i++){
        cin >> tmp;
        str.append(tmp);
    }

    cout << str;
    return 0;
}