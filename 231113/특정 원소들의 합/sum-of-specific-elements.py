nums = []
for _ in range(4): 
    nums.append(list(map(int,input().split()))) 

sum_val = 0
for i in range(4): 
    for j in range(4): 
        if i >= j: 
            sum_val += nums[i][j] 

print(sum_val)