n,m = map(int,input().split()) 

nums = [[0 for _ in range(n)] for _ in range(n)] 

for _ in range(m): 
    r,c = map(int,input().split()) 
    nums[r-1][c-1] = 1 

for i in range(n): 
    for j in range(n): 
        print(nums[i][j], end = " ")

    print()