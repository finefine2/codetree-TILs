N, S = map(int,input().split()) 
nums = list(map(int,input().split())) 
total = sum(nums) 
ans = 1000000
for i in range(N): 
    tmp = 0 
    for j in range(i+1,N): 
        tmp = total - nums[i] - nums[j] 
        ans = min(ans, abs(tmp-S))
print(ans) 

# given solution 
# 두 원소를 일일이 골라서 계산 
# N,S = map(int,input().split())
# nums = list(map(int,input().split())) 
# ans = 1e9 
# array_sum = sum(nums) 

# for i in range(N): 
#     for j in range(i+1,N): 
#         new_sum = array_sum - nums[i] - nums[j] 
#         diff = abs(new_sum-S) 
#         ans = min(diff,ans) 
# print(ans)