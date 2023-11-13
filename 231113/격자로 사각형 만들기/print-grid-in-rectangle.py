n = int(input()) 
nums = [[0 for _ in range(n)] for _ in range(n)] 

for i in range(n): 
    nums[i][0] = 1 
    nums[0][i] = 1 

    for j in range(1,n): 
        nums[i][j] = nums[i-1][j-1] + nums[i-1][j] + nums[i][j-1] 

for i in range(n): 
    for j in range(n): 
        print(nums[i][j],end=" ")
    print()