# nums =list(map(int,input().split())) 
# N = len(nums) 
# total = sum(nums)
# min_ans = 1e9 
# flag = False 
# for i in range(N): 
#     for j in range(i+1,N): 
#         for k in range(j+1,N): 
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


nums = list(map(int,input().split())) 
N = len(nums) 
total = sum(nums)
min_ans = 1e9 
flag = False 

for i in range(N): 
    for j in range(i+1,N): 
        # 1명, 2명, 2명으로 팀을 나누는 경우를 고려
        for k in range(N): 
            if k != i and k != j:
                sum1 = nums[i] 
                sum2 = nums[j] + nums[k] 
                sum3 = total - sum1 - sum2 
                # 각 팀의 능력치가 모두 다른 경우에만 능력 차이를 계산
                if sum1 != sum2 and sum2 != sum3 and sum3 != sum1: 
                    min_ans = min(min_ans, max(sum1, sum2, sum3) - min(sum1, sum2, sum3))
                    flag = True 

if flag:
    print(min_ans)
else:
    print(-1)