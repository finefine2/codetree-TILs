n = int(input()) 

nums = [[0 for _ in range(n)] for _ in range(n)] 

for i in range(n): 
    nums[i][0] = i + 1 
    for j in range(1,n): 
        nums[i][j] = nums[i][0] + n * j 

for i in range(n): 
    for elem in nums[i]: 
        print(elem,end=" ") 
    print()