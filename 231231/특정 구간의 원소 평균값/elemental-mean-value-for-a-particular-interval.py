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
    for j in range(i+1,N):
        avg_val = sum(nums[i:j+1]) // (j+1 - i) 
        if avg_val in nums[i:j+1]: 
            cnt += 1 
print(cnt)