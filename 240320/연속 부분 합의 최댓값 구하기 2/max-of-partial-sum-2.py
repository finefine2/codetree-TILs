n = int(input())

arr = list(map(int, input().split()))

ans = 0
idx = 0
s = 0

while idx < n:

    if s + arr[idx] < 0:
        ans = max(ans, s)
        idx += 1
        s = 0
    else:
        s += arr[idx]
        idx += 1
        ans = max(ans, s)


print(ans)