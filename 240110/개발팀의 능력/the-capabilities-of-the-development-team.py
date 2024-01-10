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
MAX_N  = 5

# 변수 선언 및 입력:
n = MAX_N
arr = list(map(int, input().split()))
total_sum = 0


def diff(i, j, k):
    # i가 한 팀, (j, k)가 둘이서 한 팀, 나머지 두 명이 둘이서 한 팀일 경우의 능력 차이를 리턴합니다. 
    return_value = INT_MAX

    # 세 번째 팀원의 합은 전체에서 첫 번째와 두 번째 팀원의 합을 빼주면 됩니다.
    sum1 = arr[i]
    sum2 = arr[j] + arr[k]
    sum3 = total_sum - arr[i] - arr[j] - arr[k]

    # 하나라도 합이 같은 팀이 있으면 불가능한 경우입니다.
    if sum1 == sum2 or sum2 == sum3 or sum3 == sum1:
        return return_value
    
    # 세 팀의 능력 중 최대에서 세 팀의 능력 중 최소를 뺍니다.
    return max(max(sum1, sum2), sum3) - min(min(sum1, sum2), sum3)


for elem in arr:
    total_sum += elem

# 첫 번째 팀원 i와 두 번째 팀원 j, k를 골라줍니다.
min_diff = INT_MAX
for i in range(n):
    for j in range(n):
        for k in range(n):
            if i != j and j != k and i != k:
                min_diff = min(min_diff, diff(i, j, k))

# 만들 수 없는 경우에는 초기값인 INT_MAX 그대로 남아 있습니다.
# 이 때 -1을 출력합니다.
if min_diff == INT_MAX:
    print(-1)
else:
    print(min_diff)