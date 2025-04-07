N,M = map(int,input().split())
clinics = []
board = []
viruses = 0  # 바이러스 개수 카운트

for r in range(N):
    board.append(list(map(int,input().split())))
    for c in range(N):
        if board[r][c] == 2:
            clinics.append((r,c))
        elif board[r][c] == 0:  # 바이러스 개수 세기
            viruses += 1

def gen_combin(arr,n):
    res = []
    if n==0:
        return [[]]
    for i in range(0,len(arr)):
        elem = arr[i]
        for C in gen_combin(arr[i+1:],n-1):
            res.append([elem]+C)
    return res

def in_range(r,c):
    return 0<=r<N and 0<=c<N

cands = gen_combin(clinics,M)

from collections import deque
def bfs(starts, original_board):
    q = deque()
    v = [[-1] * N for _ in range(N)]  # -1로 초기화하여 방문하지 않은 칸 표시
    remain_viruses = viruses  # 남은 바이러스 수

    # 임시 보드 생성
    board = [row[:] for row in original_board]

    # 시작점 설정
    for sr,sc in starts:
        q.append((sr,sc))
        v[sr][sc] = 0

    while q and remain_viruses > 0:
        cr,cc = q.popleft()

        for dr,dc in ((-1,0),(1,0),(0,-1),(0,1)):
            nr,nc = cr + dr, cc + dc
            if in_range(nr,nc) and v[nr][nc] == -1:
                # 벽이 아닌 경우에만 진행
                if board[nr][nc] != 1:
                    v[nr][nc] = v[cr][cc] + 1
                    q.append((nr,nc))
                    if board[nr][nc] == 0:  # 바이러스가 있는 칸인 경우
                        remain_viruses -= 1

    # 모든 바이러스를 치료하지 못한 경우
    if remain_viruses > 0:
        return float('inf')

    # 최대 시간 찾기 (바이러스가 있는 칸들 중에서만)
    max_time = 0
    for r in range(N):
        for c in range(N):
            if original_board[r][c] == 0:  # 원래 바이러스가 있던 칸에 대해서만 검사
                if v[r][c] == -1:  # 도달하지 못한 바이러스가 있는 경우
                    return float('inf')
                max_time = max(max_time, v[r][c])

    return max_time

ans = float('inf')
for c in cands:
    time = bfs(c, board)
    ans = min(ans, time)

print(-1 if ans == float('inf') else ans)