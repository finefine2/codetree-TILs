#include <iostream>
#include <string>

using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    string str;
    cin >> str;
    int len = str.length();

    str.erase(len - 2, 1);
    str.erase(1, 1);

    cout << str;

    return 0;
}