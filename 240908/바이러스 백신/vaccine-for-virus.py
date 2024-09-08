'''
선택된 m개의 병원들을 시작으로 하여 bfs를 한번 돌리는 것으로 해결
q에 시작점들을 여러 개를 담고 한번에 bfs를 돌려버린다
'''

'''
1. 활성화 시킬 위치 선정 (combinantions)
2. BFS 진행
3. 모두 다 퍼졌는지 확인

주의:
활성 바이러스가 비활성 바이러스가 있는 칸으로 가면 비활성 바이러스가 활성으로 변한다
모든 빈 칸에 바이러스를 퍼뜨리는 최소 시간(비활성이 활성 될 필욘 없음)
'''

from collections import deque
import sys

INT_MAX = sys.maxsize

N,M = tuple(map(int,input().split()))
board = []
clinics = []
for i in range(N):
    board.append(list(map(int,input().split())))
    for j in range(N):
        if board[i][j] == 2:
            clinics.append([i,j])

visited = [[0] * N for _ in range(N)]
steps = [[0] * N for _ in range(N)]
# combination 생성기
def gen_combi(arr, n):
    result = []
    if n == 0:
        return [[]]

    for i in range(0, len(arr)):
        elem = arr[i]
        for C in gen_combi(arr[i + 1:], n - 1):
            result.append([elem] + C)
    return result

selected_clinics = gen_combi(clinics,M)
def in_range(r,c):
    return 0<=r<N and 0<=c<N
def can_go(r,c):
    return in_range(r,c) and board[r][c] != 1 and not visited[r][c]

def push(r,c,new_step):
    q.append((r,c))
    visited[r][c] = True
    steps[r][c] = new_step

def initialize():
    for i in range(N):
        for j in range(N):
            visited[i][j] = 0
            steps[i][j] = 0
def bfs():
    while q:
        r,c = q.popleft()
        drs, dcs = [0,1,0,-1],[1,0,-1,0]
        for dr,dc in zip(drs,dcs):
            nr,nc = r + dr, c + dc
            if can_go(nr,nc):
                push(nr,nc,steps[r][c]+1)
    max_dist = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == 0:
                if visited[i][j]:
                    max_dist = max(max_dist,steps[i][j])
                else:
                    max_dist = INT_MAX
    return max_dist

ans = INT_MAX
q = deque()
for i in range(len(selected_clinics)):
    initialize()
    clinic = selected_clinics[i]
    for r,c in clinic:
        push(r,c,0)
    max_time = bfs()
    ans = min(max_time,ans)

if ans == INT_MAX:
    ans = -1
print(ans)