n = int(input())
nums = list(map(int,input().split())) 
new_nums = sorted(nums) 

num = new_nums[0] 

for i in range(len(new_nums)): 
    if num != new_nums[i]: 
        num = new_nums[i] 
        break
idx = 0 
for i in range(len(nums)): 
    if num == nums[i]: 
        idx = i 
        break 
        
if nums.count(num) != 1 or n == 1: 
    print(-1) 
else: 
    print(idx+1)