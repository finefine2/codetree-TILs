n = int(input())
arr = list(map(int, input().split()))

ans = 0
s = 0
for i in range(n):
    if s + arr[i] >= 0:
        s += arr[i]
        ans = max(ans, s)
    else:
        ans = max(ans, s)
        s = arr[i]

print(ans)