N = int(input()) 
sects = [] 
for _ in range(N): 
    x1,x2 = map(int,input().split()) 
    sects.append((x1,x2)) 
ans = 101 
for i in range(N): 
    Min = 101 
    Max = 0 
    for j in range(N): 
        if i == j: 
            continue
        Min = min(sects[j][0], Min) 
        Max = max(sects[j][1], Max) 
    ans = min(ans, Max - Min) 
print(ans)