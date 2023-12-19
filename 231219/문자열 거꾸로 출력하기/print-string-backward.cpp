#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    while(true){
        string tmp;

        cin >> tmp;
        if(tmp == "END") 
            break;

        reverse(tmp.begin(), tmp.end());
        cout << tmp << endl;
    }
    return 0;
}