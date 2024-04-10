from collections import deque
dir = [(-1,0),(0,-1),(0,1),(1,0)] # 북 서 동 남
N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
customer = {}
customerlist = []  # 딕셔너리에 쉽게 접근하기 위한 리스트

time = 1
while True:

    # 1. 이동
    for i in customerlist:
        if i in customer:
            visited = [[False]*N for _ in range(N)]
            visited[customer[i][0]][customer[i][1]] = True
            q = deque([(customer[i][0],customer[i][1],-1,-1)])  # 뒤는 첫 좌표 표시용

            while q:
                x, y, dx, dy = q.popleft()
                if (x,y) == (customer[i][2],customer[i][3]):
                    customer[i][0], customer[i][1] = dx, dy

                    # 2. 편의점 도착
                    if (dx,dy) == (customer[i][2], customer[i][3]):
                        graph[dx][dy] = -1
                        del customer[i]
                    break
                for j in range(4):
                    nx, ny = x+dir[j][0], y+dir[j][1]
                    if 0<=nx<N and 0<=ny<N and not visited[nx][ny] and graph[nx][ny] != -1:
                        visited[nx][ny] = True
                        if (dx,dy) == (-1,-1): q.append((nx,ny,nx,ny))
                        else: q.append((nx,ny,dx,dy))

    # 3. t번 사람 투입
    if 0<time<M+1:
        visited = [[False]*N for _ in range(N)]
        a, b = map(int, input().split())
        q = deque([(a-1,b-1)])
        visited[a-1][b-1] = True
        while q:
            x, y = q.popleft()
            if graph[x][y] == 1:
                graph[x][y] = -1  # 사람이 들어간 베이스캠프.
                customer[time] = [x,y,a-1,b-1]  # 처음 베이스캠프 = 현재위치, 목적지인 편의점
                customerlist.append(time)
                break
            for i in range(4):
                nx, ny = x+dir[i][0], y+dir[i][1]
                if 0<=nx<N and 0<=ny<N and not visited[nx][ny] and graph[nx][ny] != -1:  # 이미 꽉 차서 못가는곳은 -1로 표시해줄 예정
                    visited[nx][ny] = True
                    q.append((nx,ny))

    if not customer:
        print(time)
        break
    time += 1