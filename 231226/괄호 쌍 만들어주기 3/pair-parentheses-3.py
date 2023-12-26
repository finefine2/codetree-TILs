# N = int(input()) 
# nums = list(map(int,input().split())) 

# max_sum = 0 
# for i in range(N): 
#     for j in range(i+1,N): 
#         nums[i], nums[j] = nums[i] * 2, nums[j] * 2 
#         sum_diff = 0 
#         for k in range(N-1): 
#             sum_diff += abs(nums[k+1] - nums[k])
#         max_sum = max(max_sum,sum_diff) 
#         nums[i], nums[j] = nums[i] // 2, nums[j] // 2 
# print(max_sum) 
'''
)(())())
'''

A = input() 
cnt = 0 
for i in range(len(A)): 
    for j in range(i+1,len(A)): 
        if A[i] == "(" and A[j] == ")":
            cnt += 1 
print(cnt)