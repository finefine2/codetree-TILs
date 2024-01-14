# 선분이 겹치는 경우를 지정해야 하는데 
# 1. 지정한 선분이 비교 선분보다 x1이 크고, x2가 작은 경우 
# 2. 지정한 선분이 비교 선분보다 x1이 작고, x2가 큰 경우 

N = int(input()) 
lines = [tuple(map(int,input().split())) for _ in range(N)]

ans = 0 
# 다른 선분과 겹치지 않는 선분의 수
for i in range(N): 
    # i번째 선분이 다른 선분과 안 겹치는지 확인
    overlap = False 
    for j in range(N): 
        if j == i: 
            continue 
        if (lines[i][0] <= lines[j][0] and lines[i][1] >= lines[j][1]) or (lines[i][0] >= lines[i][1] and lines[i][1] <= lines[j][1]): 
            overlap = True 
            break 
    if overlap == False: 
        ans += 1 
print(ans)