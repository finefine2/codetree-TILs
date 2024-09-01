N = int(input())
board = [list(map(int,input().split())) for _ in range(N)]

drs,dcs = [-1,-1,1,1],[1,-1,-1,1]

def in_range(r,c):
    return 0<=r<N and 0<=c<N
def rect(r,c,a,b):
    num = 0
    turn = [a,b,a,b]
    for i in range(4):
        for j in range(turn[i]):
            r += drs[i]
            c += dcs[i]
            if not in_range(r,c):
                return 0
            num += board[r][c]
    return num
ans = []
# r,c를 시작으로 1,2,3,4 방향 
# 순서대로 k,l,k,l만큼 이동하면 그려지는 직사각형을 잡아보기? 
for r in range(N):
    for c in range(N):
        for k in range(1,N):
            for l in range(1,N):
                ans.append(rect(r,c,k,l))
print(max(ans))