N = int(input())

board = [list(map(int,input().split())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]

def in_range(r,c):
    return 0<=r<N and 0<=c<N
cnt = 0
def dfs(r,c):
    global cnt
    drs,dcs = [1,0,-1,0], [0,1,0,-1]
    for dr,dc in zip(drs,dcs):
        nr,nc = r + dr, c + dc

        if in_range(nr,nc) and not visited[nr][nc] and board[nr][nc] == board[r][c]:
            visited[nr][nc] = 1
            cnt += 1
            dfs(nr,nc)
ans = []
for r in range(N):
    for c in range(N):
        if not visited[r][c] and board[r][c]:
            visited[r][c] = 1
            cnt = 1
            dfs(r,c)
            ans.append(cnt)

bomb = 0
for a in ans:
    if a > 4:
        bomb += 1
print(bomb, max(ans))