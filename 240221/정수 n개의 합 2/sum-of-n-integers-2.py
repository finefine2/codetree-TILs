n, k = map(int, input().split())

arr = list(map(int, input().split()))

s = [0] * (n+1)

s[0] = arr[0]
for i in range(1, n):
    s[i] = s[i-1] + arr[i]

ans = 0
for i in range(n):
    for j in range(i+1, n):
        if j < i + k:
            ans = max(ans, s[j] - s[i] + arr[i])

print(ans)