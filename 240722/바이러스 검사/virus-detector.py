N = int(input()) 

rest = list(map(int,input().split())) 

L, T = map(int,input().split()) 


ans = 0 

# 먼저 팀장은 무조건 한명씩이라도 사용함 
# 고객수는 레스토랑마다 존재함 
for r in rest: 
    # 오로지 한명 있는 팀장은 일단 제거 
    r -= L
    ans += 1 

    # 만약 식당에 손님수가 남았다는 가정 하에 
    if r > 0:
        if r % T == 0: 
            ans += (r // N) 
        else: 
            ans += (r // N) + 1 
print(ans)