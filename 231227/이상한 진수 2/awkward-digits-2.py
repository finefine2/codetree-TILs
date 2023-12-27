# my solution. pretty tough, but it works 
# 1. 한 숫자를 바꾼다 
# 2. 10진법으로 계산한다 
# 3. 최댓값 갱신한다 

# N = input() 

# def change_num(n): 
#     if n == "1": 
#         n = "0"
#     elif n == "0":
#         n = "1"
#     return n 

# def convert_ten(n): 
#     ans = 0 
#     for i in range(len(n)): 
#         ans += (2 ** (len(n) - i-1)) * int(n[i])
#     return ans 

# pos = [] 
# cand1 = change_num(N[0]) + N[1:] 
# cand2 = N[:len(N)-1] + change_num(N[len(N)-1])
# pos.append(cand1)
# pos.append(cand2)
# for i in range(1,len(N)-1): 
#     cand = N[:i] + change_num(N[i]) + N[i+1:] 
#     pos.append(cand)

# max_num = -1e9 
# for p in pos:
#     max_num = max(max_num, convert_ten(p))
# print(max_num)

# given solution 
# 이진수의 가장 왼쪽 자릿수부터 차례대로 0 또는 1을 하나씩 바꾸고 값을 비교 
# 자릿수를 바꾼 뒤, 원래대로 돌려놓아야 다음 자릿수를 바꿀 때 겹치지 않음 
import sys 
INT_MIN = -sys.maxsize 

binary = list(map(int,list(input()))) 

ans = INT_MIN

for i in range(len(binary)): 
    # change i-th num
    binary[i] = 1 - binary[i] 
    # convert to decimal 
    num = 0 
    for j in range(len(binary)): 
        num = num * 2 + binary[j] 

    ans = max(ans, num) 
    # return i-th num value 
    binary[i] = 1 - binary[i] 
print(ans)