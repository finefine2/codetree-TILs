n, r, c = map(int, input().split())

arr = []
for i in range(n):
    tmp = list(map(int, input().split()))
    arr.append(tmp)

dx = [-1,1,0,0]
dy = [0,0,-1,1]

ans = []
r -= 1
c -= 1
ans.append((r, c))
while True:
    check = False
    for i in range(4):
        if 0<=r<n and 0<=c<n and 0<=r + dx[i]<n and 0<=c+dy[i]<n:
            if arr[r][c] <= arr[r + dx[i]][c + dy[i]]:
                r = r + dx[i]
                c = c + dy[i]
                check = True
                ans.append((r, c))
                break
    if not check:
        break

for k in ans:
    print(arr[k[0]][k[1]], end = " ")