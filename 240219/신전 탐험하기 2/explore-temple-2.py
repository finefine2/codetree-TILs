n = int(input())


arr = []
for i in range(n):
    l, m, r = map(int, input().split())
    arr.append((l, m, r))

dp = [[[0 for _ in range(3)] for _ in range(3)] for _ in range(n)]

for i in range(3):
    # for j in range(3):
    #     if i != j:  # 1층과 n층에서 같은 방을 선택하지 않는 조건
    dp[0][i][i] = arr[0][i]

for i in range(1, n):
    for j in range(3):  # 이전 층의 방 선택
        for k in range(3):  # 현재 층의 방 선택
            for l in range(3):  # 다음 층에서 고려할 방 선택
                if k != l:  # 연속하여 같은 방을 선택하지 않는 조건
                    dp[i][j][l] = max(dp[i][j][l], dp[i-1][j][k] + arr[i][l])

# 최종 층에서의 최대 보물 개수 찾기
result = 0
for i in range(3):
    for j in range(3):
        if i != j:  # 1층과 n층에서 같은 방을 선택하지 않는 조건
            result = max(result, dp[n-1][i][j])

print(result)