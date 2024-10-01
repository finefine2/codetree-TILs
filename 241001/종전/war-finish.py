N = int(input())

board = [list(map(int,input().split())) for _ in range(N)]

tot = sum(map(sum,board))
ans = 100 * N * N

def cal(sr,sc,d1,d2):
    v = [[0] * N for _ in range(N)]
    alst = [0] * 5
    v[sr][sc] = 1
    c1=c2=sc
    for dr in range(1,d1+d2+1):
        if dr <= d1: c1 -= 1
        else: c1 += 1
        if dr <= d2: c2 += 1
        else: c2 -= 1
        v[sr+dr][c1:c2+1] = [1]*(c2-c1+1)
    # 1~4
    for r in range(N):
        for c in range(N):
            if v[r][c] == 1: continue
            if r<sr+d1 and c<=sc: alst[0] += board[r][c]
            if r<=sr+d2 and sc<c: alst[1] += board[r][c]
            if sr+d1<=r and c<sc-d1+d2: alst[2] += board[r][c]
            if sr+d2<r and sc-d1+d2<=c: alst[3] += board[r][c]
    alst[4] = tot-sum(alst)
    return max(alst) - min(alst)



for sr in range(N-2):
    for sc in range(1,N-1):
        for d1 in range(1,N):
            if 0<=sr+d1<N and 0<=sc-d1<N:
                for d2 in range(1,N):
                    if 0<=sr+d1+d2<N and sc+d2<N:
                        ans = min(ans,cal(sr,sc,d1,d2))
print(ans)