N = int(input()) 
p = [list(map(int,input().split())) for _ in range(N)] 

evening = [False for _ in range(N)] 

ans = 1e9
# 아침 저녁 간 힘듦의 차이 계산 
def calc(): 
    morning_sum = sum([
        p[i][j] 
        for i in range(N) 
        for j in range(N) 
        if not evening[i] and not evening[j]
    ])
    evening_sum = sum([
        p[i][j] 
        for i in range(N) 
        for j in range(N) 
        if evening[i] and evening[j]
    ])
    return abs(morning_sum - evening_sum)
def find_min(idx,cnt): 
    global ans 
    # 아침 저녁으로 n/2 개씩 일이 나눴을 때에만 

    if cnt == N // 2:
        ans = min(ans,calc()) 
        return 
    
    if idx == N: 
        return 
    
    find_min(idx+1,cnt) 

    evening[idx] = True 
    find_min(idx+1,cnt+1) 
    evening[idx] = False
find_min(0,0) 
print(ans)