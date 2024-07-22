# R 식당 개수 
# P 식당 별 사람 수 
R = int(input()) 
P = list(map(int,input().split())) 
# l 리더 검사인원 
# m 팀원 검사인원 
l, m = map(int,input().split()) 
ans = 0 
 
for p in P: 
    p -= l 
    ans += 1 
    if p > 0: 
        if p % m == 0: 
            ans += p // m 
        else: 
            ans += p // m + 1
print(ans)