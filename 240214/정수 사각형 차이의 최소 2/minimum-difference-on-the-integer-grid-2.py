n = int(input())

arr = []
for i in range(n):
    tmp = list(map(int, input().split()))
    arr.append(tmp)


dpMin = [[101] * n for _ in range(n)]
dpMax = [[0] * n for _ in range(n)]

dpMin[0][0] = arr[0][0]
dpMax[0][0] = arr[0][0]

for i in range(1, n):
    dpMin[i][0] = min(dpMin[i-1][0], arr[i][0])
    dpMax[i][0] = max(dpMax[i-1][0], arr[i][0])

# 첫 번째 행 초기화
for j in range(1, n):
    dpMin[0][j] = min(dpMin[0][j-1], arr[0][j])
    dpMax[0][j] = max(dpMax[0][j-1], arr[0][j])




# 최대값을 최소로 만들기
# 최소값을 최대로 만들기
# for i in range(1, n):
#     for j in range(1, n):
#         dpMin[i][j] = min(dpMin[i][j], max(arr[i-1][j], arr[i][j-1]))

# for i in range(1, n):
#     for j in range(1, n):
#         dpMax[i][j] = max(dpMin[i][j], min(arr[i-1][j], arr[i][j-1]))

for i in range(1, n):
    for j in range(1, n):
        dpMin[i][j] = min(max(dpMin[i-1][j], dpMin[i][j-1]), arr[i][j])
        dpMax[i][j] = max(min(dpMax[i-1][j], dpMax[i][j-1]), arr[i][j])


print(abs(dpMax[n-1][n-1] - dpMin[n-1][n-1]))