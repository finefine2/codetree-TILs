n = int(input())

arr = [0] * 6010

idx = 3000
for _ in range(n):
    a, b = map(str, input().split())
    if b == 'R':
        for i in range(idx, idx + int(a)):
            arr[i] += 1
        idx += int(a)
    else:
        for i in range(idx-int(a), idx):
            arr[i] += 1
        idx -= int(a)

ans = 0
for k in arr:
    if k >= 2:
        ans += 1
print(ans)