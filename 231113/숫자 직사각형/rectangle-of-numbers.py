n,m = map(int,input().split()) 

nums = [[0 for _ in range(m)] for _ in range(n)]

start = 1 

for i in range(n): 
    for j in range(m): 
        nums[i][j] = start
        start += 1 

for i in range(n): 
    for n in nums[i]: 
        print(n,end=" ") 
    print()