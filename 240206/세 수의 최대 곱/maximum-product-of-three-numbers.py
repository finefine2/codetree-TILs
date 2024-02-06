N = int(input()) 
nums = list(map(int,input().split())) 

ans = -1e9 

for i in range(N): 
    for j in range(N): 
        for k in range(N): 
            if i == j or j == k or i == k: 
                continue 
            ans = max(ans,nums[i]*nums[j]*nums[k]) 
print(ans)