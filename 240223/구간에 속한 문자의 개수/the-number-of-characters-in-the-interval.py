# n, m, k = map(int, input().split())

# arr = []
# for i in range(n):
#     st = input()
#     arr.append(st)

# for i in range(k):
#     r1, c1, r2, c2 = map(int, input().split())


n, m, k = map(int, input().split())

arr = [input() for _ in range(n)]

pre_sum = {'a': [[0] * (m + 1) for _ in range(n + 1)],
           'b': [[0] * (m + 1) for _ in range(n + 1)],
           'c': [[0] * (m + 1) for _ in range(n + 1)]}

# 각각 a,b,c에 대해서 누적합을 구해준다.

for i in range(1, n + 1):
    for j in range(1, m + 1):
        for char in 'abc':
            pre_sum[char][i][j] = pre_sum[char][i-1][j] + pre_sum[char][i][j-1] - pre_sum[char][i-1][j-1]
            # pre_sum을 계산해주고, 전의 알파벳일 경우 그 char에 대해서 다음에 1 증가시켜준다.
            if arr[i-1][j-1] == char:
                pre_sum[char][i][j] += 1

for _ in range(k):
    r1, c1, r2, c2 = map(int, input().split())
    result = []
    for char in 'abc':
        total = pre_sum[char][r2][c2] - pre_sum[char][r2][c1-1] - pre_sum[char][r1-1][c2] + pre_sum[char][r1-1][c1-1]
        result.append(total)
    print(*result)