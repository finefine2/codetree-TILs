N = int(input()) 
nums = list(map(int,input().split()))

profit = -10000

for i in range(len(nums)): 

    for j in range(i+1): 
        if profit < nums[i] - nums[j]: 
            profit = nums[i] - nums[j] 

if profit < 0: 
    print(0)
else: 
    print(profit)