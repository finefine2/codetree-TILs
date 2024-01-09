n = int(input())

arr = [0] * 6010

idx = 0
for i in range(n):
    a, b = map(str, input().split())
    if b == 'R':
        for i in range(idx, idx + int(a)):
            arr[i+1000] += 1
        idx += int(a)
    else:
        for i in range(idx, idx - int(a), -1):
            arr[i+1000] += 1
        idx -= int(a)

ans = 0
for k in arr:
    if k >= 2:
        ans += 1
print(ans)