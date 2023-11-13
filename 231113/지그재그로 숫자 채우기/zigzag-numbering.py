n,m = map(int,input().split())

start = 0 
nums = [[0 for _ in range(m)] for _ in range(n)]

for j in range(m): 
    if j % 2 == 0: 
        for i in range(n): 
            nums[i][j] = start
            start += 1
    else: 
        for i in range(n-1,-1,-1): 
            nums[i][j] = start
            start += 1 

for i in range(n): 
    for a in nums[i]: 
        print(a,end=" ")
    print()