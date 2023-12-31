# N = int(input())
# nums = list(map(float,input().split())) 
# cnt = 0 
# for i in range(N): 
#     for j in range(i,N):
#         avg_val = sum(nums[i:j+1]) / (j+1 - i)
#         exists = False 
#         if avg_val in nums[i:j+1]: 
#             exists = True 
#         if exists: 
#             cnt += 1
# print(cnt)

N = int(input())
nums = list(map(int,input().split())) 

cnt = 0 
for i in range(N): 
    for j in range(i,N): 
        sum_interval = 0 
        for k in range(i,j+1): 
            sum_interval += nums[k] 
        avg = sum_interval / (j+1-i) 
        exists = False
        for k in range(i,j+1): 
            if nums[k] == avg: 
                exists = True 
        if exists: 
            cnt += 1 
print(cnt)