nums = [[0] * 4 for _ in range(4)]

for i in range(4): 
    nums[i] = list(map(int,input().split())) 

for n in nums: 
    print(sum(n))