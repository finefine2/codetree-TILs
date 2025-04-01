N,M = map(int,input().split())

board = [list(map(int,input().split())) for _ in range(N)]
movements = []
for _ in range(M):
    d,p = map(int,input().split())
    movements.append((d-1,p))
supples = [(N-1,0),(N-1,1),(N-2,0),(N-2,1)]

drs = [0,-1,-1,-1,0,1,1,1]
dcs = [1,1,0,-1,-1,-1,0,1]
def move_supple(d,p,supples):
    ans = []
    for sr,sc in supples:
        nr = (sr + drs[d] * p) % N
        nc = (sc + dcs[d] * p) % N
        ans.append((nr,nc))
    return ans

def in_range(r,c):
    return 0<=r<N and 0<=c<N

def check_diag(supples):
    for s in supples:
        sr,sc = s[0],s[1]
        cnt = 0
        for dr,dc in ((-1,-1),(-1,1),(1,-1),(1,1)):
            nr,nc = sr + dr, sc + dc
            if in_range(nr,nc) and board[nr][nc] >= 1:
                cnt += 1
        board[sr][sc] += cnt

for i in range(M):
    d,p = movements[i]
    #[1] 영양제를 이동시킨다
    supples = move_supple(d,p,supples)

    #[2] 영양제를 이동시키고 해당 위치에 영양제 투입
    for i in supples:
        sr,sc = i[0],i[1]
        board[sr][sc] += 1
        # supples.pop(i)

    #[3] 영ㅇ양제 주입받은 리브로수 근처 나무들 성장시키기 1만큼
    check_diag(supples)

    #[4] 영양제 주입받은 리브로수 제외 높이 2이상인 리브로수들 찾고
    # 해당 나무들 2씩 감소시키기 + 그 위치에 영양제 투입 하고 싸이클 반복
    new_supples = []
    for r in range(N):
        for c in range(N):
            if (r,c) not in supples and board[r][c] >= 2:
                board[r][c] -= 2
                new_supples.append((r,c))
    supples = new_supples
ans = 0 

for b in board: 
    ans += sum(b) 
print(ans) 

