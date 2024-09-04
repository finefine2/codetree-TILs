N,M = tuple(map(int,input().split()))
board = [list(map(int,input().split())) for _ in range(N)]


def in_range(r,c):
    return 0<=r<N and 0<=c<N
def find_pos(num):
    ans = (-1,-1)
    for r in range(N):
        for c in range(N):
            if board[r][c] == num:
                ans = (r,c)
    return ans

def get_max_pos(i,j):
    drs,dcs=[-1,-1,-1,0,1,1,1,0],[-1,0,1,1,1,0,-1,-1]
    max_ans,max_pos = -1, (-1,-1)
    for dr,dc in zip(drs,dcs):
        nr,nc = i + dr, j + dc
        if in_range(nr,nc) and board[nr][nc] > max_ans:
            max_ans = board[nr][nc]
            max_pos = (nr,nc)
    return max_pos
def swap(r,c,nr,nc):
    (r,c),(nr,nc) = (nr,nc),(r,c)
    board[r][c],board[nr][nc] = board[nr][nc],board[r][c]
def move():
    for i in range(1,N*N+1):
        r,c = find_pos(i)
        nr,nc = get_max_pos(r,c)
        swap(r,c,nr,nc)



for _ in range(M):
    move()

for r in range(N):
    for c in range(N):
        print(board[r][c],end=" ")
    print()