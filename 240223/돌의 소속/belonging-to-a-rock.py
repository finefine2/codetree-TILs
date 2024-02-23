n, q = map(int, input().split())

arr = []
for i in range(n):
    a = int(input()) - 1  # 0, 1, 2
    arr.append(a)

dp = [[0] * 3 for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(3):
        # 이전까지의 누적 개수 + 현재 돌이 j그룹에 속할 경우 1 증가
        dp[i][j] = dp[i - 1][j] + (arr[i-1] == j)


for i in range(q):
    a, b = map(int, input().split())
    result = [0] * 3
    for j in range(3):
        result[j] = dp[b][j] - dp[a - 1][j]

    print(*result)





# # 입력 받기
# N, Q = map(int, input().split())

# # 각 그룹별로 돌의 누적 개수를 저장할 리스트 초기화
# # 각 그룹의 누적 개수를 저장하기 위해 N+1의 크기를 가지는 0으로 초기화된 리스트 생성
# # 첫 번째 인덱스는 사용하지 않기 위해 N+1의 크기를 사용
# cumulative_sums = [[0] * (N + 1) for _ in range(3)]

# # 돌의 그룹 정보 입력 받으면서 누적합 업데이트
# for i in range(1, N + 1):
#     group = int(input()) - 1  # 그룹 번호를 0, 1, 2로 조정
#     for j in range(3):
#         # 현재 그룹에 대해서만 1 증가, 나머지 그룹은 이전 값 복사
#         cumulative_sums[j][i] = cumulative_sums[j][i - 1] + (1 if j == group else 0)

# # 질의 처리
# for _ in range(Q):
#     a, b = map(int, input().split())
#     result = []
#     for j in range(3):
#         # 각 그룹별로 a-1까지의 누적 개수를 b까지의 누적 개수에서 빼서
#         # a부터 b까지의 그룹별 돌의 개수를 구함
#         result.append(cumulative_sums[j][b] - cumulative_sums[j][a - 1])
#     print(*result)