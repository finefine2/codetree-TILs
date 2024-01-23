N = int(input()) 
heights = [int(input()) for _ in range(N)] 

ans = 0 
for i in range(1,1001): 
    cnt = 0 
    if heights[0] > i: 
        cnt += 1 
    for j in range(1,N): 
        if heights[j] > i and heights[j-1] <= i: 
            cnt += 1
    ans = max(ans,cnt) 
print(ans)