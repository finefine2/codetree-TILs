# N = int(input()) 
# nums = list(map(int,input().split())) 

# max_sum = 0 
# for i in range(N): 
#     for j in range(i+1, N): 
#         for k in range(j+1, N): 
#             nums[i],nums[j],nums[k] = nums[i]*2,nums[j]*2,nums[k]*2
#             sum_diff = 0 
#             for l in range(N-1): 
#                 sum_diff += abs(nums[l+1] - nums[l]) 
#             max_sum = max(max_sum, sum_diff) 
#             nums[i],nums[j],nums[k] = nums[i] // 2, nums[j] // 2, nums[k] // 2 
# print(max_sum)

N = int(input()) 
cows = list(map(int,input().split()))
cnt = 0 
for i in range(N): 
    for j in range(i+1,N): 
        for k in range(j+1,N): 
            if cows[i] <= cows[j] <= cows[k]: 
                cnt += 1 
print(cnt)