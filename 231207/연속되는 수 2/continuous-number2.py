N = int(input())
nums =[]
for _ in range(N): 
    nums.append(int(input())) 
max_num = -10
cnt = 0 

if N == 1: 
    print(1)
else:
    for i in range(len(nums)-1): 
        if nums[i] == nums[i+1]:
            cnt += 1
        else: 
            cnt = 0
        max_num = max(cnt,max_num)
    print(max_num+1)