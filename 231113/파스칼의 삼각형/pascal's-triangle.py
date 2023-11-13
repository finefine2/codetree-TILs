n = int(input()) 
nums = [[0 for _ in range(n)] for _ in range(n)]

start = 1 

for i in range(n): 
    nums[i][0] = 1 
    nums[i][i] = 1 
    for j in range(1,i): 
        nums[i][j]  = nums[i-1][j] + nums[i-1][j-1] 
for i in range(n): 
    for j in range(n): 
        if nums[i][j] > 0: 
            print(nums[i][j],end=" ") 
    print()