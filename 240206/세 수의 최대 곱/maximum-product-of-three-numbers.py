N = int(input()) 
nums = list(map(int,input().split())) 
nums.sort() 
plus, minus, zero = 0, 0, 0

for n in nums: 
    if n > 0:
        plus += 1 
    elif n == 0: 
        zero += 1
    else: 
        minus += 1
ans = 0 
if max(nums) == 0: 
    ans = 0 
elif minus == 0: 
    ans = nums[-1] * nums[-2] * nums[-3] 
elif plus == 0: 
    ans = nums[-1] * nums[-2] * nums[-3] 
elif plus == 1: 
    ans = nums[0] * nums[1] * nums[-1] 
elif N == 3: 
    ans = nums[0] * nums[1] * nums[2] 
else: 
    ans = max(nums[0] * nums[1] * nums[-1], nums[-1] * nums[-2] * nums[-3])
print(ans) 
# 3개
# 양양양 -> 제일 크게
# 양음음 -> 제일 크게
# 음음음 -> 제일 작게
# 양양음 -> 제일 작게
# ans = -1e9 

# 완탐 
# for i in range(N): 
#     for j in range(N): 
#         for k in range(N): 
#             if i == j or j == k or i == k: 
#                 continue 
#             ans = max(ans,nums[i]*nums[j]*nums[k]) 
# print(ans)