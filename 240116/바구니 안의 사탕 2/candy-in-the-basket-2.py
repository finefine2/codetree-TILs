n, k = map(int, input().split())

arr = [0] * 220
for i in range(n):
    a, b = map(int, input().split())
    arr[b] += a

Max = -1
for i in range(100):
    ans = 0
    for j in range(i - k, i + k + 1):
        if j >= 0 and j <= 100:
            ans += arr[j]
    if ans > Max:
        Max = ans

print(Max)