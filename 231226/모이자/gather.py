# N = int(input()) 
# arr = list(map(int,input().split()))

# max_sum = 0 
# for i in range(N): 
#     arr[i] *= 2 
#     sum_diff = 0 
#     for j in range(N-1): 
#         sum_diff += abs(arr[j+1] - arr[j]) 
#     max_sum = max(max_sum, sum_diff) 
#     arr[i] //= 2 
# print(max_sum) 

N = int(input()) 
nums = list(map(int,input().split())) 

min_sum = 1e9 
'''
1-1 + 1-2 + 1-3 + 1-4 
nums[0] * (0-0) + nums[1] * (0-1) + nums[2] * (0-2) + nums[3] * (0-3) + nums[4] * (0-4) 

'''
ans = [] 
for i in range(N): 
    sum_diff = 0
    for j in range(N): 
        sum_diff += nums[j] * abs(i-j)
    ans.append(sum_diff)
print(min(ans))