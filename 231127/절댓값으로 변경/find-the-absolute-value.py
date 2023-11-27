N = int(input()) 
nums = list(map(int,input().split())) 

# for n in nums: 
#     print(abs(n), end=" ")

def absolute_val(nums): 
    for i in range(N): 
        if nums[i] < 0: 
            nums[i] = -nums[i] 
    return 
absolute_val(nums) 

for elem in nums: 
    print(elem,end=" ")