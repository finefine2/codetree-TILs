#include <iostream>
#include <string>

using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    string str, re_str, str1, str2;
    int num1, num2;
    cin >> str1 >> str2;

    str = str1 + str2;
    re_str = str2 + str1;

    num1 = stoi(str);
    num2 = stoi(re_str);

    cout << num1 + num2;
    return 0;
}