#include <iostream>
#include <string>

using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.

    int n, tmp, sum=0;
    cin >> n;

    for (int i=0; n>i; i++){
        cin >> tmp;
        sum += tmp;
    }

    string answer = to_string(sum);
    answer = answer.substr(1) + answer.substr(0, 1);
    cout << answer;


    return 0;
}