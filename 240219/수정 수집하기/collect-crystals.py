# n, k = map(int, input().split())

# s = input()
# st = " " + s

# dp = [[[0 for _ in range(3)] for _ in range(k+2)] for _ in range(n+2)]

# import sys
# MIN = -sys.maxsize
# for i in range(n+1):
#     for j in range(k+1):
#         dp[i][j][0] = MIN
#         dp[i][j][1] = MIN
    
# # dp[0][0][0] = 0
# # dp[0][1][1] = 0
# # for i in range(n):
# #     for j in range(k+1):
# #         if dp[i][j][0] != MIN:
# #             if st[i+1] == 'L':
# #                 dp[i+1][j][0] = max(dp[i+1][j][0], dp[i][j][0] + 1)
# #                 dp[i+1][j+1][1] = max(dp[i+1][j+1][1], dp[i][j][0])
# #             else:
# #                 dp[i+1][j][0] = max(dp[i+1][j][0], dp[i][j][0] + 1)
# #                 dp[i+1][j+1][1] = max(dp[i+1][j+1][1], dp[i][j][0])

# #         if dp[i][j][1] != MIN:
# #             if st[i+1] == 'L':
# #                 dp[i+1][j+1][0] = max(dp[i+1][j+1][0], dp[i][j][1] + 1)
# #                 dp[i+1][j][1] = max(dp[i+1][j][1], dp[i][j][1])
# #             else:
# #                 dp[i+1][j+1][0] = max(dp[i+1][j+1][0], dp[i][j][1])
# #                 dp[i+1][j][1] = max(dp[i+1][j][1], dp[i][j][1] + 1)
# # 초기 조건 수정
# dp[0][0][0] = 0  # 엘라가 왼쪽 샘터에 있고, 아직 이동하지 않았을 때
# dp[0][1][1] = 0
# for i in range(n):
#     for j in range(k+1):
#         if dp[i][j][0] != MIN:
#             if st[i+1] == 'L':
#                 dp[i+1][j][0] = max(dp[i+1][j][0], dp[i][j][0] + 1)  # 왼쪽에 있고 왼쪽에서 수정이 떨어짐
#             else:
#                 dp[i+1][j+1][1] = max(dp[i+1][j+1][1], dp[i][j][0])  # 왼쪽에서 오른쪽으로 이동
                
#         if dp[i][j][1] != MIN:
#             if st[i+1] == 'R':
#                 dp[i+1][j][1] = max(dp[i+1][j][1], dp[i][j][1] + 1)  # 오른쪽에 있고 오른쪽에서 수정이 떨어짐
#             else:
#                 dp[i+1][j+1][0] = max(dp[i+1][j+1][0], dp[i][j][1])  # 오른쪽에서 왼쪽으로 이동

# ans = 0
# for i in range(k+1):
#     ans = max(ans, dp[n][i][0])
#     ans = max(ans, dp[n][i][1])

# print(ans)

# n, k = map(int, input().split())
# s = input()

# # dp[i][j][l] : i번째 수정까지 고려했을 때, j번 이동하고, l=0이면 왼쪽, l=1이면 오른쪽에 있을 때의 최대 수정 수
# dp = [[[0 for _ in range(2)] for _ in range(k+1)] for _ in range(n+1)]

# # 초기 위치는 왼쪽 샘터이므로, dp[0][0][0] = 0으로 시작 (수정을 하나도 수집하지 않음)
# # 오른쪽 샘터에 대한 초기값은 설정할 필요가 없으며, 이동 없이 시작하므로 k=0의 경우만 고려

# for i in range(1, n+1):
#     for j in range(k+1):
#         # 현재 위치가 왼쪽 샘터일 경우
#         if s[i-1] == 'L':  # 수정이 왼쪽에 떨어지면 수집 가능
#             dp[i][j][0] = max(dp[i][j][0], dp[i-1][j][0] + 1)  # 이동하지 않고 수집
#         else:
#             if j > 0:  # 이동할 수 있다면 오른쪽에서 왼쪽으로 이동하여 수집
#                 dp[i][j][0] = max(dp[i][j][0], dp[i-1][j-1][1] + 1)

#         # 현재 위치가 오른쪽 샘터일 경우
#         if s[i-1] == 'R':  # 수정이 오른쪽에 떨어지면 수집 가능
#             dp[i][j][1] = max(dp[i][j][1], dp[i-1][j][1] + 1)  # 이동하지 않고 수집
#         else:
#             if j > 0:  # 이동할 수 있다면 왼쪽에서 오른쪽으로 이동하여 수집
#                 dp[i][j][1] = max(dp[i][j][1], dp[i-1][j-1][0] + 1)

#         # 이동하지 않고 위치만 유지하는 경우도 고려하여 최대값을 갱신
#         dp[i][j][0] = max(dp[i][j][0], dp[i-1][j][0])
#         dp[i][j][1] = max(dp[i][j][1], dp[i-1][j][1])

# # 최대 수정 수집 개수 찾기
# answer = 0
# for j in range(k+1):
#     answer = max(answer, dp[n][j][0], dp[n][j][1])

# print(answer)

n, k = map(int, input().split())
s = input()

# dp 배열의 정의를 수정하여, 각 상태에서의 최적의 해를 저장
# dp[i][j][0 or 1]에서 0은 왼쪽 샘터에 있을 때, 1은 오른쪽 샘터에 있을 때를 나타냄
dp = [[[-1 for _ in range(2)] for _ in range(k+1)] for _ in range(n+1)]
dp[0][0][0] = 0  # 시작점은 왼쪽 샘터에 있고, 아직 이동하지 않았으며, 수정을 수집하지 않았다.

for i in range(1, n + 1):
    for j in range(k + 1):
        if s[i - 1] == 'L':  # 수정이 왼쪽에 떨어지는 경우
            dp[i][j][0] = max(dp[i][j][0], dp[i - 1][j][0] + 1)  # 왼쪽에 있으면 수정을 수집
            if j > 0:
                dp[i][j][0] = max(dp[i][j][0], dp[i - 1][j - 1][1])  # 오른쪽에서 왼쪽으로 이동한 경우, 수정은 수집하지 않음
        else:
            if j > 0:
                dp[i][j][0] = max(dp[i][j][0], dp[i - 1][j - 1][1] + 1)  # 오른쪽에서 왼쪽으로 이동해서 수정 수집

        if s[i - 1] == 'R':  # 수정이 오른쪽에 떨어지는 경우
            dp[i][j][1] = max(dp[i][j][1], dp[i - 1][j][1] + 1)  # 오른쪽에 있으면 수정을 수집
            if j > 0:
                dp[i][j][1] = max(dp[i][j][1], dp[i - 1][j - 1][0])  # 왼쪽에서 오른쪽으로 이동한 경우, 수정은 수집하지 않음
        else:
            if j > 0:
                dp[i][j][1] = max(dp[i][j][1], dp[i - 1][j - 1][0] + 1)  # 왼쪽에서 오른쪽으로 이동해서 수정 수집

        # 이동하지 않고 위치를 유지하는 경우
        dp[i][j][0] = max(dp[i][j][0], dp[i - 1][j][0])
        dp[i][j][1] = max(dp[i][j][1], dp[i - 1][j][1])

answer = 0
for j in range(k + 1):
    answer = max(answer, dp[n][j][0], dp[n][j][1])

print(answer)