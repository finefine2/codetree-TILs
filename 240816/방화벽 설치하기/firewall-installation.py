from collections import deque

def getInput():
    # 입력받는 함수
    global N, M, R, graph, firelist, wallcandlist
    N, M = map(int, input().split())
    graph = []
    firelist = []
    wallcandlist = []

    for i in range(N):
        a = list(map(int, input().split()))
        for j in range(M):
            if a[j] == 0:
                wallcandlist.append((i,j))
            elif a[j] == 2:
                firelist.append((i,j))
        graph.append(a)

    R = len(wallcandlist)

def fire(walllist):
    # 불을 전파하며 영역을 세어주는 함수
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    temp_graph = [[arr for arr in arrs] for arrs in graph]

    for x, y in walllist:
        temp_graph[x][y] = 1

    for xx, yy in firelist:
        q = deque([(xx,yy)])

        while q:
            x, y = q.popleft()

            for i in range(4):
                nx = x+dx[i]
                ny = y+dy[i]
                if 0<=nx<N and 0<=ny<M and temp_graph[nx][ny] == 0:
                    temp_graph[nx][ny] = 2
                    q.append((nx,ny))
    ccnt = 0
    for i in range(N):
        for j in range(M):
            if temp_graph[i][j] == 0:
                ccnt += 1
    return ccnt

def dfs(level, index):
    # dfs를 실행하는 함수
    global cnt
    if level == 3:
        cnt = max(cnt, fire(walllist))
        return
    for i in range(index, R):
        walllist.append(wallcandlist[i])
        dfs(level+1, i+1)
        walllist.pop()


# ===== 실제 실행하는 부분 =====
def main():
    global cnt, walllist

    cnt = -1
    walllist = []
    getInput()
    dfs(0, 0)
    print(cnt)

main()