# N = int(input()) 
# arr = list(map(int,input().split()))

# max_sum = 0 
# for i in range(N): 
#     arr[i] *= 2 
#     sum_diff = 0 
#     for j in range(N-1): 
#         sum_diff += abs(arr[j+1] - arr[j]) 
#     max_sum = max(max_sum, sum_diff) 
#     arr[i] //= 2 
# print(max_sum) 

N = int(input()) 
nums = list(map(int,input().split())) 

min_sum = 1e9 
'''
1-1 + 1-2 + 1-3 + 1-4 
'''
for i in range(N): 
    pos = nums[i] 
    sum_dif = 0 
    for j in range(N-1): 
        sum_dif += (j) * abs(nums[j+1] - nums[j]) 
    min_sum = min(min_sum,sum_dif) 
print(min_sum+1)