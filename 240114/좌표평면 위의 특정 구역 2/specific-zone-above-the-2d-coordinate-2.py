N = int(input()) 

ans = 1e9 
points = [] 
for _ in range(N): 
    r,c = map(int,input().split()) 
    points.append([r,c]) 

for i in range(N): 
    min_r, min_c = 50000,50000
    max_r, max_c = 0,0
    for j in range(N): 
        if j == i: 
            continue
        
        r,c = points[j][0], points[j][1] 
        min_r = min(min_r,r) 
        min_c = min(min_c,c) 
        max_r = max(max_r,r) 
        max_c = max(max_c,c) 

    ans = min(ans, abs(max_r-min_r) * abs(max_c-min_c))
print(ans)