#include <iostream>
#include <string>

using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    string str1, str2;
    int len;

    cin >> str1 >> str2;
    len = str2.length();

    while (str1.find(str2) != string::npos){
        auto idx = str1.find(str2);
        str1.erase(idx, len);
    }
    cout << str1;

    return 0;
}