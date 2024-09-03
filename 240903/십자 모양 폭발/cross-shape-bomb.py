N = int(input())

board = [list(map(int,input().split())) for _ in range(N)]

r,c = tuple(map(int,input().split()))
r -= 1
c -= 1
bomb_length = board[r][c]
bomb_length -= 1
def in_range(r,c):
    return 0<=r<N and 0<=c<N

def find_board(r,c,l):
    start_r,start_c = r,c
    for s_r in range(r-l,r+l+1):
        if in_range(s_r,start_c):
            board[s_r][start_c] = 0
    for s_c in range(c-l,c+l+1):
        if in_range(start_r,s_c):
            board[start_r][s_c] = 0

find_board(r,c,bomb_length)
# gravity
temp = [[0] * N for _ in range(N)]

for c in range(N):
    start_row = N-1
    for r in range(N-1,-1,-1):
        if board[r][c] != 0:
            temp[start_row][c] = board[r][c]
            start_row -= 1
for r in range(N):
    for c in range(N):
        board[r][c] = temp[r][c]

for r in range(N):
    for c in range(N):
        print(board[r][c],end=" ")
    print()