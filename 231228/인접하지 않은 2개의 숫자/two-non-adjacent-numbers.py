N = int(input()) 
nums = list(map(int,input().split())) 
ans = -1e9
for i in range(N):
    for j in range(i+2,N): 
        ans = max(ans, nums[i] + nums[j]) 
print(ans)