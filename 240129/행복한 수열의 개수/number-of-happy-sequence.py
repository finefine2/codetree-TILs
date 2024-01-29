n, m = map(int, input().split())

arr = []
for i in range(n):
    st = list(map(int, input().split()))
    arr.append(st)

ans = 0
for i in range(n):
    cnt = 0
    for j in range(n-1):
        if arr[i][j] == arr[i][j+1]:
            cnt += 1
    if cnt == m-1:
        ans += 1

for i in range(n):
    cnt = 0
    for j in range(m-1):
        if arr[j][i] == arr[j+1][i]:
            cnt += 1
    if cnt == m-1:
        ans += 1

print(ans)