from collections import deque

N,K,U,D = tuple(map(int,input().split()))
board = [list(map(int,input().split())) for _ in range(N)]
board_pos = [(i,j) for i in range(N) for j in range(N)]

# print(board_pos)
visited = [[0] * N for _ in range(N)]
def initialize_visit():
    for i in range(N):
        for j in range(N):
            visited[i][j] = 0


# 최댓값 갱신
# combination
def gen_combi(arr,n):
    res = []
    if n == 0:
        return [[]]
    for i in range(0,len(arr)):
        elem = arr[i]
        for C in gen_combi(arr[i+1:],n-1):
            res.append([elem] + C)
    return res
# print(gen_combi(board_pos,K))

def in_range(r,c):
    return 0<=r<N and 0<=c<N

def can_move(r,c,target_num):
    if in_range(r,c) and not visited[r][c] and U <= abs(board[r][c] - target_num) <= D:
        return True
    return False

def bfs():
    drs, dcs = [1,0,-1,0],[0,1,0,-1]
    while q:
        r,c = q.popleft()
        target_num = board[r][c]
        for dr,dc in zip(drs,dcs):
            nr,nc = r + dr, c + dc
            if can_move(nr,nc,target_num):
                visited[nr][nc] = 1
                q.append((nr,nc))

def calc_visit():
    cnt = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j]:
                cnt += 1
    return cnt
visit_points = gen_combi(board_pos,K)
max_ans = -1
for i in range(len(visit_points)):
    # 조합 개수만큼 루프를 돌린다
    # 정해진 좌표들을 q에 넣고 bfs를 돌린다
    # 시작도시를 포함하여 값을 구한다
    initialize_visit()
    q = deque()
    starts = visit_points[i]
    for sr,sc in starts:
        q.append((sr,sc))
        visited[sr][sc] = 1
    bfs()
    mid = calc_visit()
    if mid > max_ans:
        max_ans = mid
print(max_ans)