# my solution 
# N = int(input())
# nums =[]
# for _ in range(N): 
#     nums.append(int(input())) 
# max_num = -10
# cnt = 0 

# if N == 1: 
#     print(1)
# else:
#     for i in range(len(nums)-1): 
#         if nums[i] == nums[i+1]:
#             cnt += 1
#         else: 
#             cnt = 0
#         max_num = max(cnt,max_num)
#     print(max_num+1)

# given solution 
n = int(input()) 
arr = list(int(input()) for _ in range(n))

# 연속해서 동일한 숫자가 나오는 횟수를 구하고, 그 중 최댓값 갱신 
ans, cnt = 0, 0 
for i in range(n): 
    # case 1 
    if i >= 1 and arr[i] == arr[i-1]: 
        cnt += 1 
    # case 2 
    else: 
        cnt = 1 
    ans = max(ans,cnt)
print(ans)