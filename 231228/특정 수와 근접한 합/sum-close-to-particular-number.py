N, S = map(int,input().split()) 
nums = list(map(int,input().split())) 
total = sum(nums) 
ans = 1000000
for i in range(N): 
    tmp = 0 
    for j in range(i+1,N): 
        tmp = total - nums[i] - nums[j] 
        ans = min(ans, abs(tmp-S))
print(ans)