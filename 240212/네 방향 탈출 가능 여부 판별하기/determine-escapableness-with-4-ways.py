from collections import deque

n, m = map(int, input().split())

arr = []
for i in range(n):
    tmp = list(map(int, input().split()))
    arr.append(tmp)

q = deque()
check = [[0] * m for _ in range(n)]
ans = [[0] * m for _ in range(n)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def isin(a, b):
    return 0<=a<n and 0<=b<m

num = 1
escape = 0
def BFS():
    global num
    global escape 
    
    while q:
        x, y = q.popleft()

        if x == n-1 and y == m-1:
            escape = 1
            return

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if isin(nx, ny) and not check[nx][ny] and arr[nx][ny] == 1:
                check[nx][ny] = 1
                ans[nx][ny] = num
                num += 1
                q.append((nx, ny))


check[0][0] = 1
num += 1
q.append((0,0))
BFS()

print(escape)