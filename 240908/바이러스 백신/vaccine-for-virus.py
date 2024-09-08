import copy
from collections import deque

N,M = tuple(map(int,input().split()))
# 0 virus, 1 wall, 2 hospital
board = []
clinics = []
for i in range(N):
    board.append(list(map(int,input().split())))
    for j in range(N):
        if board[i][j] == 2:
            clinics.append([i,j])

visited = [[-1] * N for _ in range(N)]
# steps = [[-1] * N for _ in range(N)]
new_board = copy.deepcopy(board)
def initialize_visit():
    for r in range(N):
        for c in range(N):
            visited[r][c] = 0
def initialize_board():
    for r in range(N):
        for c in range(N):
            board[r][c] = new_board[r][c]
# def initialize_step():
#     for r in range(N):
#         for c in range(N):
#             steps[r][c] = -1
def in_range(r,c):
    return 0<=r<N and 0<=c<N
def can_move(r,c):
    return in_range(r,c) and not visited[r][c] and board[r][c] != 1
def push(r,c,num):
    visited[r][c] = num+1
    board[r][c] = 2
    # steps[r][c] = new_step + 1
    q.append((r,c))
def bfs():
    drs,dcs = [-1,1,0,0],[0,0,-1,1]
    while q:
        r,c = q.popleft()
        num = visited[r][c]
        for dr,dc in zip(drs,dcs):
            nr,nc = r + dr, c + dc
            if can_move(nr,nc):
                push(nr,nc,num)
def get_time():
    max_ans = -1
    for r in range(N):
        for c in range(N):
            if max_ans < visited[r][c]:
                max_ans = visited[r][c]
    return max_ans
def count_virus():
    ans = 0
    for r in range(N):
        for c in range(N):
            if board[r][c] == 0:
                ans += 1
    if ans == 0:
        return True
    else:
        return False

def gen_combi(arr,n):
    res = []
    if n == 0:
        return [[]]
    for i in range(len(arr)):
        elem = arr[i]
        for C in gen_combi(arr[i+1:],n-1):
            res.append([elem]+C)
    return res
candidates = gen_combi(clinics,M)
# print(candidates)
ans = 10000
# for i in range(len(candidates)):
#     print(f"this turn is {i+1}")
#     hos = candidates[i]
#     for r,c in hos:
#         print(r,c)
for i in range(len(candidates)):
    # 0. 초기화
    initialize_visit()
    initialize_board()
    # initialize_step()
    q = deque()
    # 1. 병원을 선택한다
    hos = candidates[i]
    # 1-1. q에 append한다
    # 1-2. 방문처리 한다
    # 1-3. step 값들에 0을 추가해준다
    for r,c in hos:
        q.append((r,c))
        visited[r][c] = 0
    # 2. 선택된 병원들로부터 bfs처리를 한다
    bfs()

    # 3. 모든 바이러스가 제거됐다는 가정하에, 바이러스가 제거되는 시간을 계산한다
        # 3-0. 최대 steps를 return한다
        # 3-1. 최솟값을 계속해서 갱신한다
        # 3-2. 만약 바이러스를 다 제거못한다면 -1을 내놓는다
    if count_virus():
        cnt = get_time()
        if cnt < ans:
            ans = cnt
    else:
        ans = -1
if ans <= 0:
    print(ans)
else:
    print(ans-1)