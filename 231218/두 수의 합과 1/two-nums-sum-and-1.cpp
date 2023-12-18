#include <iostream>
#include <string>

using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int n1, n2;
    string str;

    cin >> n1 >> n2;

    n1 += n2;

    str = to_string(n1);

    int cnt=0;

    for (int i= 0; str[i] != '\0'; i++)
        if (str[i] == '1')
            cnt++;

    cout << cnt;
    
    return 0;
}