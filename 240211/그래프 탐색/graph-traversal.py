n, m = map(int, input().split())

arr = [[0] * (n+1) for _ in range(n+1)]
for i in range(m):
    x, y = map(int, input().split())
    # arr.append((x, y))
    arr[x][y] = 1
    arr[y][x] = 1
    
ans = 0
check = [0] * (n+1)
def DFS(start):
    global ans
    for now in arr[start]:
        if not check[now]:
            check[now] = True
            ans += 1
            DFS(now)


for i in range(1, n):
    DFS(i)

print(ans)