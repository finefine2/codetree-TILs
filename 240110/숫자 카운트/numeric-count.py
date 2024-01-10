# 각각 크기가 3인 1차원 배열로 관리한다고 생각을 한다 
# a가 생각할 숫자들을 고른 뒤, 각 위치에 있는 숫자들에 대해 b에 그 숫자가 있는지 확인
# 존재하면, 그 위치가 같은지 다른지에 따라 각각 값을 count 

def check(s,nums): 
    if s[0] == s[1] or s[0] == s[2] or s[1] == s[2]: 
        return False 
    for num in nums: 
        cnt1, cnt2 = 0,0
        for i in range(3): 
            if s[i] == num[0][i]: 
                cnt1 += 1
            elif s[i] in num[0]: 
                cnt2 += 1 
        if cnt1 != num[1] or cnt2 != num[2]: 
            return False 
    return True 

N = int(input())
numbers = [] 
for i in range(N): 
    numbers.append(list(map(int,input().split()))) 
    numbers[-1][0] = str(numbers[-1][0]) 
cnt = 0 

for i in range(123,999): 
    if check(str(i),numbers): 
        cnt += 1
print(cnt)