N = int(input()) 

nums = [0] * 30 
nums[0] = 2 
nums[1] = 4  

for i in range(len(nums)): 
    if i >= 2:
        nums[i] = (nums[i-1] * nums[i-2]) % 100

print(nums[N-1])