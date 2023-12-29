N,K = map(int,input().split()) 
nums = list(map(int,input().split())) 

max_val = 0 

for i in range(N-K+1):
    max_val = max(max_val,sum(nums[i:i+K])) 
print(max_val)

# given solution 
# max_sum = 0 
# for i in range(N-K+1): 
#     interval_sum = 0 
#     for j in range(i,i+k): 
#         interval_sum += nums[j] 
#     max_sum = max(max_sum, interval_sum) 
# print(max_sum)