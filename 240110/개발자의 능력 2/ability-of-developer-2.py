'''
완탐 조건이 생각보다 까다로운 편'''

# nums = list(map(int,input().split())) 
# total = sum(nums) 
# min_ans = 1e9 
# nums.sort() 

# for i in range(6):
#     for j in range(i+1,6): 
#         for k in range(6): 
#             if k == i or k == j: 
#                 continue
#             for l in range(k+1,6):
#                 if l == i or l == j:
#                     continue
#                 s1 = nums[i] + nums[j] 
#                 s2 = nums[k] + nums[l] 
#                 s3 = total - s1 - s2 
#                 min_ans = min(min_ans,max(s1,s2,s3) - min(s1,s2,s3))

# print(min_ans)

'''
given solution 
첫 번째 팀과 두 번째 팀을 먼저 배치하고 남은 사람들은 총합에서 빼면 됨 

1팀 2명 그리고 2팀 2명을 배치하는 완탐을 진행해서 문제를 해결하고 두 팀원이 겹치지 않아야 함 
'''
nums = list(map(int,input().split())) 
def diff(i,j,k,l): 
    # 3 팀의 합은 전체에서 1,2팀의 합을 빼주는 경우 
    sum1 = nums[i] + nums[j] 
    sum2 = nums[k] + nums[l] 
    sum3 = sum(nums) - sum1 - sum2 
    # 3팀 차이 중 최댓값을 리턴
    # 왜지? 
    ret = abs(sum1 - sum2) 
    ret = max(ret,abs(sum2-sum3)) 
    ret = max(ret,abs(sum3-sum1))
    return ret 
min_diff = 1e9 
N = len(nums) 
for i in range(N):
    for j in range(i+1,N): 
        for k in range(N): 
            for l in range(k+1,N): 
                if k == i or k == j or l == i or l == j: 
                    continue 
                min_diff = min(min_diff, diff(i,j,k,l))
print(min_diff)