import sys 
MAX_N = 1000 
N = int(input()) 
sums = list(map(int,input().split())) 

nums = [0] * N 
ans = [] 

for i in range(1,N-1): 
    nums[0] = i 

    for j in range(1,N): 
        nums[j] = sums[j-1] - nums[j-1] 
    flag = True 
    exists = [False] * (MAX_N+1) 
    for j in range(N): 
        if nums[j] <= 0 or nums[j] > N: 
            flag = False 
        else: 
            if exists[nums[j]]: 
                flag = False
            exists[nums[j]] = True 
    if flag: 
        for j in range(N): 
            print(nums[j],end=" ") 
        sys.exit()