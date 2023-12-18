#include <iostream>
#include <string>

using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int n1 = 0, n2 = 0;
    string str;

    cin >> str;

    for (int i = 0; i < str.length()-1; i++){
        if (str[i] == 'e' && str[i+1] == 'e')
            n1++;
        else if (str[i] == 'e' && str[i+1] == 'b')
            n2++;
    }
    cout << n1 << ' ' << n2;

    return 0;
}