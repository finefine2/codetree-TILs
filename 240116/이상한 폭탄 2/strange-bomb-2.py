N, K = map(int,input().split()) 
bombs = [int(input()) for _ in range(N)] 
ans = [] 
for i in range(N): 
    for j in range(N): 
        if j == i: 
            continue 
        if abs(j-i) <= K and bombs[i] == bombs[j]: 
            ans.append(bombs[i]) 
if len(ans) == 0: 
    print(-1) 
else: 
    print(max(ans))