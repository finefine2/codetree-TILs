nums =list(map(int,input().split())) 
N = len(nums) 
total = sum(nums)
min_ans = 1e9 
flag = False 
for i in range(N): 
    for j in range(N): 
        for k in range(N): 
            if i == j or i == k or j == k: 
                continue 
            sum1 = nums[i] 
            sum2 = nums[j] + nums[k] 
            sum3 = total - sum1 - sum2 
            if sum1 != sum2 and sum2 != sum3 and sum3 != sum1: 
                min_ans = min(min_ans,max(sum1,sum2,sum3)-min(sum1,sum2,sum3))
                flag = True 
if flag:
    print(min_ans)
else:
    print(-1)