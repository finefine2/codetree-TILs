# 1. 한 숫자를 바꾼다 
# 2. 10진법으로 계산한다 
# 3. 최댓값 갱신한다 

N = input() 

def change_num(n): 
    if n == "1": 
        n = "0"
    elif n == "0":
        n = "1"
    return n 

def convert_ten(n): 
    ans = 0 
    for i in range(len(n)): 
        ans += (2 ** (len(n) - i-1)) * int(n[i])
    return ans 

pos = [] 
cand1 = change_num(N[0]) + N[1:] 
cand2 = N[:len(N)-1] + change_num(N[len(N)-1])
pos.append(cand1)
pos.append(cand2)
for i in range(1,len(N)-1): 
    cand = N[:i] + change_num(N[i]) + N[i+1:] 
    pos.append(cand)

max_num = -1e9 
for p in pos:
    max_num = max(max_num, convert_ten(p))
print(max_num)