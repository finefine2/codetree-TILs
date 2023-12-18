#include <iostream>
#include <string>

using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.

    string str[10];
    char alp;
    bool flag = true;

    for (int i= 0; 10>i; i++)
    cin >> str[i];
    cin >> alp;

    for (int i= 0 ; 10>i ; i++){
        if (str[i][str[i].length()-1] == alp){
            flag = false;
            cout << str[i] << endl;
        }
        
    }

    if (flag)
    cout << "None";
    
    return 0;
}