#include <iostream>
#include <string>

using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    string str1, str2;
    char alp;
    int cnt = 0;

    cin >> str1;
    alp = str1[0];
    
    for (int i =0; str1[i] != '\0'; i++){
        
        if (alp == str1[i]){
            cnt++;
        }
        else{
            str2 += alp;
            str2 += to_string(cnt);
            alp = str1[i];
            cnt = 1;
        }
    }
    str2 += alp;
    str2 += to_string(cnt);
    cout << str2.length() << endl;
    cout << str2;
    return 0;
}