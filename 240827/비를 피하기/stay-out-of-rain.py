# M 개의 쉘터를 시작으로 하는 BFS를 한번 돌리는 것으로 해결이 됨
# 그래프에서 시작점이 하나일 때 bfs를 돌리면 그 시작으로부터 각 정점까지 도달하기 위한 최단거리를 구해주는데
# bfs 특성상 queue를 이용하기 때문에 시작으로부터 가까운 정점들을 먼저 큐에서 빼줌

# 시작점이 여러 개인 상태로 bfs를 수행하면 각각 시작으로부터 거리가 가장 가까운 정점부터 큐에서 나오게 됨
from collections import deque
N,H,M = tuple(map(int,input().split()))
board = [list(map(int,input().split())) for _ in range(N)]

s_pos = [(i,j) for i in range(N) for j in range(N) if board[i][j] == 3]
q = deque()
visited = [[0] * N for _ in range(N)]
steps = [[0] * N for _ in range(N)]

def in_range(r,c):
    return 0<=r<N and 0<=c<N
# 격자 내에서, 벽도 없고 아직 방문한 적 없으면 지금 이동하는 곳이 최단거리임으로 가야함
def can_move(r,c):
    return in_range(r,c) and board[r][c] != 1 and not visited[r][c]
# queue에 새 위치 추가하고 방문 표시, 시작점으로부터 최단거리 값도 갱신
def push(nr,nc,new_step):
    q.append((nr,nc))
    visited[nr][nc] = 1
    steps[nr][nc] = new_step

def bfs():
    while q:
        r,c = q.popleft()
        drs,dcs = [-1,1,0,0],[0,0,-1,1]
        for dr,dc in zip(drs,dcs):
            nr,nc = r + dr, c + dc
            if can_move(nr,nc):
                push(nr,nc,steps[r][c]+1)
# 비를 피하는 공간들을 시작점으로 하는 bfs 진행
# 이는 각 사람마다 가장 가까운 쉘터까지의 거리를 계산 가능하게끔
for sr,sc in s_pos:
    push(sr,sc,0)

bfs()

for i in range(N):
    for j in range(N):
        if board[i][j] != 2:
            print(0,end=" ")
        else:
            if not visited[i][j]:
                print(-1,end=" ")
            else:
                print(steps[i][j],end=" ")
    print()