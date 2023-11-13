n = int(input()) 

start = 1 

nums = [[0 for _ in range(n)] for _ in range(n)] 
if n % 2 == 0: 
    for j in range(n-1,-1,-1): 
        if j % 2 == 0: 
            for i in range(n): 
                nums[i][j] = start 
                start += 1 
        else: 
            for i in range(n-1,-1,-1):
                nums[i][j] = start
                start += 1
else: 
    for j in range(n-1,-1,-1): 
        if j % 2 == 1: 
            for i in range(n): 
                nums[i][j] = start 
                start += 1 
        else: 
            for i in range(n-1,-1,-1): 
                nums[i][j] = start
                start += 1 
                
    
for i in range(n): 
    for j in range(n): 
        print(nums[i][j],end=" ")
    print()