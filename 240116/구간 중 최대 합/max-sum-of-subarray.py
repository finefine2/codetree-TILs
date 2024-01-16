n, k = map(int, input().split())

arr = list(map(int, input().split()))

Max = -1

for i in range(n - k + 1):
    ans = 0
    for j in range(i, i+k):
        ans += arr[j]

    if Max < ans:
        Max = ans

print(Max)