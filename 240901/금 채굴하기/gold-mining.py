N,M = tuple(map(int,input().split()))
# gold 1 blank 0
board = [list(map(int,input().split())) for _ in range(N)]

def get_expense(k):
    return k*k + (k+1) * (k+1)

def in_range(r,c):
    return 0<=r<N and 0<=c<N

def get_board(start_r,start_c):
    cnt = 0
    for i in range(N):
        for j in range(N):
            if abs(start_r-i) + abs(start_c-j) and in_range(i,j) and board[i][j] == 1:
                cnt += 1
    return cnt
cnt = 0

for k in range(2*N-1):
    for r in range(N):
        for c in range(N):
            if get_board(r,c) * M - get_expense(k) > 0:
                cnt = max(cnt,get_board(r,c))
print(cnt)