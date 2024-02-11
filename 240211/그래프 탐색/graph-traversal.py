n, m = map(int, input().split())

arr = [[] for _ in range(n + 1)]
# arr = [[0] * (n+1) for _ in range(n+1)]
for i in range(m):
    x, y = map(int, input().split())
    # arr.append((x, y))
    # arr[x][y] = 1
    # arr[y][x] = 1
    arr[x].append(y)
    arr[y].append(x)
    
ans = 0
check = [0] * (n+1)
def DFS(start):
    global ans
    for now in arr[start]:
        if not check[now]:
            check[now] = True
            ans += 1
            DFS(now)

check[1] = True
DFS(1)

print(ans)