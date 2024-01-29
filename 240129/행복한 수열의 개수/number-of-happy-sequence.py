n, m = map(int, input().split())

arr = []
for i in range(n):
    st = list(map(int, input().split()))
    arr.append(st)

ans = 0
for i in range(n):
    cnt = 0
    for j in range(n):
        for k in range(m-1):
            if arr[i][j+k] == arr[i][j+k+1]:
                cnt += 1
    if cnt == m-1:
        ans += 1

for i in range(n):
    cnt = 0
    for j in range(n):
        for k in range(m-1):
            if arr[j+k][i] == arr[j+k+1][i]:
                cnt += 1
    if cnt == m-1:
        ans += 1

print(ans)