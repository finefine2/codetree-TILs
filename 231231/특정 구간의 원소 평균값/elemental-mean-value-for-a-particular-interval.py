N = int(input())
nums = list(map(float,input().split())) 
cnt = 0 
for i in range(N): 
    for j in range(i,N):
        avg_val = sum(nums[i:j+1]) / (j+1 - i)
        exists = False 
        if avg_val in nums[i:j+1]: 
            exists = True 
        if exists: 
            cnt += 1
print(cnt)