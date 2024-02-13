from collections import deque
n, m = map(int, input().split())

arr = []
for i in range(n):
    tmp = list(map(int, input().split()))
    arr.append(tmp)

def isin(a, b):
    return 0<=a<n and 0<=b<m
dx = [0,0,1,-1]
dy = [1,-1,0,0]

def BFS():

    num = 0
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if isin(nx, ny) and not check[nx][ny]:
                if arr[nx][ny] == 1:
                    check[nx][ny] = 1
                    num += 1
                    arr[nx][ny] = 0
                    # 0으로 바꾸어서 녹여준다.
                else:
                    check[nx][ny] = 1
                    q.append((nx, ny))
                    # 0일 경우 계속 탐색해준다.
    
    return num

last = 0
t = 0
while True:
    t += 1
    q = deque()
    check = [[0] * m for _ in range(n)]
    q.append((0,0))
    cnt = BFS()
    if cnt:
        last = cnt
    else:
        break

print(t - 1, last)