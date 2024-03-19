from collections import deque

n = int(input())

arr = []
for i in range(n):
    tmp = list(map(int, input().split()))
    arr.append(tmp)

check = [[0] * n for _ in range(n)]

def isin(a, b):
    return 0<=a<n and 0<=b<n

def BFS(i, j, dist):
    check = [[0] * n for _ in range(n)]

    q = deque()
    q.append((i, j))
    check[i][j] = 1

    dx = [0,0,1,-1]
    dy = [1,-1,0,0]

    cnt = 1
    while q:
        x, y = q.popleft()
        for dir in range(4):
            nx = x + dx[dir]
            ny = y + dy[dir]

            if isin(nx, ny) and not check[nx][ny] and abs(arr[x][y] - arr[nx][ny]) <= dist:
                q.append((nx, ny))
                cnt += 1
                check[nx][ny] = 1
        
    return cnt

def find(dist):
    ans = 0
    for i in range(n):
        for j in range(n):
            if not check[i][j]:
                ans = max(ans, BFS(i, j, dist))
                # 각각 i, j에 따라서 해줄 때 개수를 구해준다.
                if ans >= (n * n + 1) // 2:
                    return True
                # 전체 칸의 수 n**2에 반 이상이 되면은 True
    return False

left = 1
right = 1000000
Min = 1000000

while left <= right:
    mid = (left + right) // 2

    if find(mid):
        Min = min(Min, mid)
        right = mid - 1
    else:
        left = mid + 1

print(Min)