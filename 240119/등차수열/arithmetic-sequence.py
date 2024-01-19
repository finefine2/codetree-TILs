N = int(input()) 
nums = list(map(int,input().split())) 
ans = 0
for i in range(1,101): 
    cnt = 0 
    for k in range(N): 
        for l in range(k+1,N): 
            if (nums[k] + nums[l]) == 2*i: 
                cnt += 1 
    ans = max(ans,cnt) 
print(ans)