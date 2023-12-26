# my solution 

# N = int(input()) 
# nums = list(map(int,input().split())) 

# min_sum = 1e9 
# '''
# 1-1 + 1-2 + 1-3 + 1-4 
# nums[0] * (0-0) + nums[1] * (0-1) + nums[2] * (0-2) + nums[3] * (0-3) + nums[4] * (0-4) 

# '''
# ans = [] 
# for i in range(N): 
#     sum_diff = 0
#     for j in range(N): 
#         sum_diff += nums[j] * abs(i-j)
#     ans.append(sum_diff)
# print(min(ans))

# given solution 
import sys 
INT_MAX = sys.maxsize
N = int(input()) 
nums = list(map(int,input().split())) 
min_dist = INT_MAX
# 각 i번째 집으로 모였을 때의 합 
for i in range(N): 
    sum_dist = 0 
    for j in range(N): 
        sum_dist += abs(j-i) * nums[j] 
    min_dist = min(min_dist,sum_dist)
print(min_dist)