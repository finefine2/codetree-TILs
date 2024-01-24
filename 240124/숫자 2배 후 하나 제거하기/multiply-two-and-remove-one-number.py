# arr = [] 
# max_diff = 0 
# for i in range(len(arr)): 
#     arr[i] *= 2 
#     for j in range(len(arr)): 
#         remaining_arr = [] 
#         for k in range(len(arr)): 
#             if k != j: 
#                 remaining_arr.append(arr[k]) 
#         # for k, elem in enumerate(arr): 
#         #     if k != j: 
#         #         remaining_arr.append(elem)
#         sum_diff = 0 
#         for k in range(len(arr) - 2): 
#             sum_diff += abs(remaining_arr[k+1] - remaining_arr[k]) 
#         max_diff = max(max_diff,sum_diff) 
#     arr[i] //= 2 
# print(max_diff)

N = int(input())
nums = list(map(int,input().split())) 

min_diff = 1e9  
for i in range(N): 
    nums[i] *= 2 
    for j in range(N): 
        remaining_arr = [] 
        for k, num in enumerate(nums): 
            if k != j: 
                remaining_arr.append(num)
        sum_diff = 0 
        for k in range(N-2): 
            sum_diff += abs(remaining_arr[k+1] - remaining_arr[k]) 
        min_diff = min(min_diff,sum_diff) 
    nums[i] //= 2 
print(min_diff)