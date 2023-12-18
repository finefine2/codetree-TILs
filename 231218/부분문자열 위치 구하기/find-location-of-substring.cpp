#include <iostream>
#include <string>

using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    string str1, str2;

    cin >> str1 >> str2;

    auto tmp = str1.find(str2);
    
    if (tmp != string::npos)
        cout << tmp;
    else
        cout << -1;
    return 0;
}