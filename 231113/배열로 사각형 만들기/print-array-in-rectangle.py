nums = [[0 for _ in range(5)] for _ in range(5)] 

for i in range(5): 
    nums[0][i] = 1 
    nums[i][0] = 1 

for i in range(1,5): 
    for j in range(1,5): 
        nums[i][j] = nums[i-1][j] + nums[i][j-1] 

for i in range(5): 
    for j in range(5): 
        print(nums[i][j],end=" ")
    print()