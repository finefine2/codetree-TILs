# nums =list(map(int,input().split())) 
# N = len(nums) 
# total = sum(nums)
# min_ans = 1e9 
# flag = False 
# for i in range(N): 
#     for j in range(N): 
#         for k in range(N): 
#             if i == j or i == k or j == k: 
#                 continue 
#             sum1 = nums[i] 
#             sum2 = nums[j] + nums[k] 
#             sum3 = total - sum1 - sum2 
#             if sum1 != sum2 and sum2 != sum3 and sum3 != sum1: 
#                 min_ans = min(min_ans,max(sum1,sum2,sum3)-min(sum1,sum2,sum3))
#                 flag = True 
# if flag:
#     print(min_ans)
# else:
#     print(-1)

'''
첫, 두 팀 팀원들 결정하면 나머지는 결정된다 늘 그렇듯이 
각 팀원의 능력치 계산해 모두 다른 경우에 대해 팀간 능력 차이 구하고 그 중 최소 출력 
'''
import sys 
INT_MAX = sys.maxsize
min_ans = 1e9 
nums = list(map(int,input().split())) 
N = len(nums) 
total_sum = 0 
def diff(i,j,k): 
    # i 가 한 팀 j,k 가 둘이서 한팀, 나머지 둘이서 한 팀일 경우의 능력 차이 리턴 
    return_value = min_ans
    sum1 = nums[i]
    sum2 = nums[j] + nums[k] 
    sum3 = total_sum - sum1 - sum2
    # 하나라도 합이 같은 팀이 있으면 불가능 
    if sum1 == sum2 or sum2 == sum3 or sum3 == sum1: 
        return return_value
    # 세 팀의 능력 최댓값 - 최솟값 
    return max(max(sum1,sum2),sum3) - min(min(sum1,sum2),sum3) 

for num in nums: 
    total_sum += num 
min_diff = INT_MAX
for i in range(n):
    for j in range(n):
        for k in range(n):
            if i != j and j != k and i != k:
                min_diff = min(min_diff, diff(i, j, k))
if min_diff == INT_MAX: 
    print(-1) 
else: 
    print(min_diff)