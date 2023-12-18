#include <iostream>
#include <string>

using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    string str;
    char tmp, s1, s2;
    int N, n1, n2, q;

    cin >> str >> N;

    for (int i = 0; N > i; i++){
        cin >> q;

        if (q == 1){
            cin >> n1 >> n2;
            n1--;
            n2--;

            tmp = str[n1];
            str[n1] = str[n2];
            str[n2] = tmp;
            cout << str << endl;
        }
        else if (q == 2){
            cin >> s1 >> s2;
            for (int i = 0; str[i] != '\0'; i++){
                if(str[i] == s1)
                    str[i] = s2;
            }
            cout << str << endl;
        }
    }
    return 0;
}