N = int(input()) 
nums = list(map(int,input().split())) 

max_num = -1 

for n in nums: 
    if max_num < n: 
        cnt = 0 
        for elem in nums: 
            if elem == n: 
                cnt += 1 
    if cnt == 1: 
        max_num = n 
print(max_num)