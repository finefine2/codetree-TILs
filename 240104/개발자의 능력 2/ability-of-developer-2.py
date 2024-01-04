# nums = list(map(int,input().split())) 
# total = sum(nums)
# sum1,sum2,sum3 = 0,0,0 
# min_ans = 1e9 
# def get_diff(i,j,k,l): 
#     sum1 = nums[i] + nums[j] 
#     sum2 = nums[k] + nums[l] 
#     sum3 = sum(nums) - sum1 - sum2 
#     max_sum = max(sum1,sum2,sum3) 
#     min_sum = min(sum1,sum2,sum3) 
#     return max_sum - min_sum

# for i in range(6): 
#     for j in range(i+1,6): 
#         for k in range(j+1,6): 
#             for l in range(k+1,6): 
#                 print(i,j,k,l)
#                 min_ans = min(min_ans,get_diff(i,j,k,l))
# print(min_ans)




def calculate_team_difference(abilities):
    min_difference = float('inf')  # 초기 최소 차이 설정

    # 가능한 모든 팀 배정 조합 생성
    for i in range(1, 6):
        for j in range(i + 1, 6):
            for k in range(j + 1, 6):
                team1_sum = abilities[0] + abilities[i]
                team2_sum = abilities[1] + abilities[j]
                team3_sum = abilities[2] + abilities[k]
                difference = max(team1_sum, team2_sum, team3_sum) - min(team1_sum, team2_sum, team3_sum)

                # 최소 차이 갱신
                if difference < min_difference:
                    min_difference = difference

    return min_difference

# 개발자들의 알고리즘 능력 입력 받기
abilities = list(map(int,input().split()))
# 팀의 능력 총합 차이 계산
min_difference = calculate_team_difference(abilities)

# 결과 출력
print(min_difference)