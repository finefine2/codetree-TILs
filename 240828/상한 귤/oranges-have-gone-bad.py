# from collections import deque
#
# N,K = tuple(map(int,input().split()))
# board = []
# rotten_oranges = []
# healthy_oranges = []
# ans = [[0] * N for _ in range(N)]
# for i in range(N):
#     board.append(list(map(int,input().split())))
#     for j in range(N):
#         if board[i][j] == 0:
#             ans[i][j] = -1
#         elif board[i][j] == 1:
#             healthy_oranges.append((i,j))
#         elif board[i][j] == 2:
#             rotten_oranges.append((i, j))
#             ans[i][j] = 0
#
# visited = [[0] * N for _ in range(N)]
# steps = [[0] * N for _ in range(N)]
#
# def in_range(r,c):
#     return 0<=r<N and 0<=c<N
#
# def push(nr,nc,new_step):
#     q.append((nr,nc))
#     visited[nr][nc] = 1
#     steps[nr][nc] = new_step
#
# def bfs():
#     drs,dcs = [1,0,-1,0],[0,1,0,-1]
#     while q:
#         r,c = q.popleft()
#         for dr,dc in zip(drs,dcs):
#             nr,nc = r + dr, c + dc
#             if in_range(nr,nc) and not visited[nr][nc] and board[nr][nc] != 0:
#                 push(nr,nc,steps[r][c]+1)
#
# q=deque()
# for rr,rc in rotten_oranges:
#     push(rr,rc,0)
# bfs()
#
# for r in range(N):
#     for c in range(N):
#         if (r,c) in healthy_oranges:
#             if steps[r][c] == 0:
#                 ans[r][c] = -2
#             else:
#                 ans[r][c] = steps[r][c]
# for a in ans:
#     print(*a)

'''
아래는 답지 풀이인데, 좀 더 효율적인가..? 큰 틀에서의 접근은 같은듯
'''

# BFS를 돌릴 때 여러 시작점을 두어, 걸리는 시간을 기록하면 각 칸으로부터 가장 가까운 시작점으로부터 걸리는 시간이 구해짐
# 시작점이 하나일 때 BFS를 돌리면 그 점으로부터 각 점까지 도달하기 위한 최단시간을 구하는 건
# q를 이용하기 때문에 시작점으로부터 거리가 더 가까운 정점들을 먼저 q에서 빼주기 때문

# 가중치가 동일한 그래프에서 시작점이 여러개인 bfs를 수행하게 되면 각각의 시작점으로부터 거리가 가장 가까운 정점부터 큐에서 나오기 때문에
# 초기에 주어진 상한 귤들로부터 각 신선한 귤마다 최초로 상하게 되는 시간이 한번의 BFS로 구해짐

from collections import deque
N,K = tuple(map(int,input().split()))
board = [list(map(int,input().split())) for _ in range(N)]

rotten_oranges = [(i,j)
                  for i in range(N)
                  for j in range(N)
                  if board[i][j] == 2]

q = deque()
visited = [[0] * N for _ in range(N)]
steps = [[0] * N for _ in range(N)]

def in_range(r,c):
    return 0<=r<N and 0<=c<N

def can_move(r,c):
    return in_range(r,c) and not visited[r][c] and board[r][c]
# q에 새로운 위치를 추가하고 방문 표시
# 상하게 되는 시간 값도 갱신
def push(nr,nc,new_step):
    q.append((nr,nc))
    visited[nr][nc] = 1
    steps[nr][nc] = new_step

# bfs를 통해 칸마다 최초로 상하는 시간을 구함
def bfs():
    # q에 남은 것이 없을 때까지
    while q:
        r,c = q.popleft()
        drs,dcs = [1,0,-1,0],[0,1,0,-1]
        for dr,dc in zip(drs,dcs):
            nr,nc = r + dr, c + dc
            # 아직 방문한 적 없으면서 갈 수 있으면 q에 넣음
            if can_move(nr,nc):
                push(nr,nc,steps[r][c]+1)

# 처음 상해있던 귤들의 위치를 q에 append
# 각 칸에 있는 신선한 귤에 대해 가장 가까이 있던 상한 귤로부터 최초로 상하게 되는 시간을 단 한번의 bfs로 가능케
for r,c in rotten_oranges: 
    push(r,c,0) 
bfs() 

for r in range(N): 
    for c in range(N): 
        if board[r][c] == 0: 
            print(-1,end=" ") 
        else: 
            # 그러네, 마지막 부분 갱신되는 게 어차피 도달하지 못하면 not visited 상태일테니 
            if not visited[r][c]: 
                print(-2,end=" ")
            else: 
                print(steps[r][c],end=" ")
    print()