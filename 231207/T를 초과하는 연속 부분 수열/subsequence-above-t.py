n,t = map(int,input().split()) 
nums = list(map(int,input().split())) 
ans, cnt = 0, 0 
for i in range(len(nums)): 

    if i >= 1 and nums[i] > t and nums[i-1] > t: 
        cnt += 1
    else: 
        cnt = 1 
    ans = max(ans,cnt) 
if cnt == 1: 
    print(0)
else: 
    print(ans)