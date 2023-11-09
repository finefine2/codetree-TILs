for i in range(5): 
    nums = list(input().split())

for i in range(5): 
    for j in range(3): 
        print(nums[i][j])
        nums[i][j] = nums[i][j].upper()

for n in nums: 
    print(n)