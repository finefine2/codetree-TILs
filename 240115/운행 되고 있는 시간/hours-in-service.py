N = int(input())

points = [tuple(map(int,input().split())) for _ in range(N)]

ans = -1e9 

for i in range(N): 
    lines = [0] * 1001
    for j in range(N): 
        if j == i: 
            continue
        a,b = points[j] 
        for k in range(a,b): 
            lines[k] = 1
    ans = max(ans,sum(lines))
print(ans)