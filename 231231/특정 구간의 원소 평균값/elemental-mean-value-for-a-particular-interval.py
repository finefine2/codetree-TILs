# N = int(input()) 
# nums = list(map(int,input().split())) 

# max_sum = 0 
# for i in range(N): 
#     for j in range(i,N): 
#         sum_val = 0 
#         for k in range(i,j+1): 
#             sum_val += nums[k] 
#         max_sum = max(max_sum,sum_val)
# print(max_sum)

N = int(input())
nums = list(map(int,input().split())) 
cnt = 0 

for i in range(N): 
    for j in range(i,N):
        avg_val = int(sum(nums[i:j+1]) / len(nums[i:j+1]))

        if avg_val in nums[i:j]: 
            cnt += 1 
print(cnt)