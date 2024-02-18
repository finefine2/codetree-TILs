n = int(input())
soccer = [0] * (n + 1)
baseball = [0] * (n + 1)
for i in range(1, n + 1):
    soccer[i], baseball[i] = map(int, input().split())

# dp[i][j][k] :: 지금까지 앞 i명의 학생을 보며, 축구부에 j명을, 야구부에 k명을 선택했을 때 나올 수 있는 능력의 합의 최대
dp = [[[0 for _ in range(10)] for _ in range(15)] for _ in range(1005)]

for i in range(n):
    for s in range(12):
        for b in range(10):
            # 현재 상태를 다음 상태로 전이시킵니다.
            dp[i + 1][s][b] = max(dp[i + 1][s][b], dp[i][s][b])

            # 축구 점수를 추가할 수 있는 경우를 고려합니다.
            if s != 11:
                dp[i + 1][s + 1][b] = max(dp[i + 1][s + 1][b], dp[i][s][b] + soccer[i + 1])

            # 야구 점수를 추가할 수 있는 경우를 고려합니다.
            if b != 9:
                dp[i + 1][s][b + 1] = max(dp[i + 1][s][b + 1], dp[i][s][b] + baseball[i + 1])

print(dp[n][11][9])
# 원래 내가 푸려고 했던 방식,, 답안을 참고했다.


# ************************************
# ********* 처음 낸 정답 ****************
# ************************************

# def maximize_ability(n, abilities):
#     # 각 학생의 축구와 야구 능력치를 따로 저장하는 리스트
#     foot = [ability[0] for ability in abilities]
#     base = [ability[1] for ability in abilities]

#     # 축구팀과 야구팀의 인원수 상한은 각각 11명, 9명이므로 이를 초과하지 않도록 설정
#     max_football_players = min(11, n)
#     max_baseball_players = min(9, n)

#     # DP 배열 초기화
#     # dp[i][j][k]: i번째 학생까지 고려하고, 축구팀에 j명, 야구팀에 k명을 선택했을 때의 최대 능력치 합
#     dp = [[[-1] * (max_baseball_players + 1) for _ in range(max_football_players + 1)] for _ in range(n + 1)]

#     # DP를 통해 최대 능력치 합 구하기
#     def dp_maximize_ability(idx, football_players, baseball_players):
#         if idx == n:
#             return 0
#         if dp[idx][football_players][baseball_players] != -1:
#             return dp[idx][football_players][baseball_players]

#         # 현재 학생을 축구팀에 추가하는 경우
#         football_option = 0
#         if football_players < max_football_players:
#             football_option = foot[idx] + dp_maximize_ability(idx + 1, football_players + 1, baseball_players)

#         # 현재 학생을 야구팀에 추가하는 경우
#         baseball_option = 0
#         if baseball_players < max_baseball_players:
#             baseball_option = base[idx] + dp_maximize_ability(idx + 1, football_players, baseball_players + 1)

#         # 현재 학생을 어느 팀에도 추가하지 않는 경우
#         no_selection_option = dp_maximize_ability(idx + 1, football_players, baseball_players)

#         # 세 경우 중 최대값을 DP 배열에 저장
#         dp[idx][football_players][baseball_players] = max(football_option, baseball_option, no_selection_option)

#         return dp[idx][football_players][baseball_players]

#     # 최대 능력치 합 반환
#     return dp_maximize_ability(0, 0, 0)


# n = int(input())
# abilities = []
# for _ in range(n):
#     s, b = map(int, input().split())
#     abilities.append((s, b))

# result = maximize_ability(n, abilities)
# print(result)