n, m = map(int, input().split())

arr = []
for i in range(n):
    st = list(map(int, input().split()))
    arr.append(st)

k = 0
Max = 0

for i in range(n):
    for j in range(n):
        for k in range(2 * n - 1):
            num = 0
            for x in range(n):
                for y in range(n):
                    if abs(x - j) + abs(y - i) <= k:
                        num += arr[x][y]
            if num * m >= k * k + (k + 1) * (k + 1):
                Max = max(Max, num)

print(Max)