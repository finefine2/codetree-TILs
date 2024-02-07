N,M = map(int,input()) 
nums = list(map(int,input().split())) 
cnt, i = 0,0 
while i < N: 
    if nums[i] == 1: 
        cnt += 1 
        i += 2 * M + 1 
    else: 
        i += 1 
print(cnt)