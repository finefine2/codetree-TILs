N,M,T = tuple(map(int,input().split()))

board = [list(map(int,input().split())) for _ in range(N)]

counts = [[0] * N for _ in range(N)]
for _ in range(M):
    r,c = tuple(map(int,input().split()))
    counts[r-1][c-1] = 1

new_counts = [[0] * N for _ in range(N)]

def in_range(r,c):
    return 0<=r<N and 0<=c<N

def get_next_pos(r,c):
    # 상하좌우
    drs,dcs = [-1,1,0,0],[0,0,-1,1]
    max_pos,max_ans = -1,-1
    for dr,dc in zip(drs,dcs):
        nr,nc = r + dr, c + dc
        if in_range(nr,nc) and board[nr][nc] > max_ans:
            max_ans = board[nr][nc]
            max_pos = nr,nc
    return max_pos

def move(r,c):
    max_pos = get_next_pos(r,c)
    new_counts[max_pos[0]][max_pos[1]] += 1
def move_all():
    # new counts initialize
    for r in range(N):
        for c in range(N):
            new_counts[r][c] = 0
    for r in range(N):
        for c in range(N):
            if counts[r][c] == 1:
                move(r,c)

    for r in range(N):
        for c in range(N):
            counts[r][c] = new_counts[r][c]


def remove_duplicate():
    for r in range(N):
        for c in range(N):
            if counts[r][c] >= 2:
                counts[r][c] = 0

def simulate():
    move_all()

    remove_duplicate()

for _ in range(T):
    simulate()

ans = 0
for r in range(N):
    for c in range(N):
        ans += counts[r][c]
print(ans)