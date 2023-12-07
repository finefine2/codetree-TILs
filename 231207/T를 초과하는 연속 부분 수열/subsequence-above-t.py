n,t = map(int,input().split()) 
nums = list(map(int,input().split())) 
ans, cnt = 0, 0 
for i in range(len(nums)): 

    if nums[i] > t: 
        cnt += 1
    else: 
        cnt = 0
    ans = max(ans,cnt) 
print(ans)