# my solution 
N = int(input()) 
nums = list(map(int,input().split())) 

# # 부분집합은 원소가 2개이며 총 N개 쌍이 나오겠네 

# if N == 1: 
#     print(sum(nums))

# else: 
#     min_val = -1e9
#     nums.sort()
#     for i in range(N): 
#         mid = nums[i] + nums[2*N-i-1]
#         if mid > min_val:
#             min_val = mid
#     print(min_val)

# 배열 내의 최댓값과 최솟값을 묶는 것이 항상 최선임을 확인 

nums.sort() 
sum_max = 0 
for i in range(N): 
    # i번째와 2N-1-i번째 원소를 매칭 
    sum_mid = nums[i] + nums[2*N-1-i] 
    if sum_mid > sum_max: 
        sum_max = sum_mid 
print(sum_max)