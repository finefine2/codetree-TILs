nums = list(map(int,input().split()) 
nums.sort() 
'''
A 가 BC 사이로 
C 가 AB 사이로 
'''
if nums[0] + 1 == nums[1] and nums[1] + 1 == nums[2]: 
    print(0) 
elif nums[0] + 2 == nums[1] or nums[1] + 2 == nums[2]: 
    print(1) 
else: 
    print(2)