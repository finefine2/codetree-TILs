n, m, t = map(int, input().split())

arr = []
for i in range(n):
    tmp = list(map(int, input().split()))
    arr.append(tmp)

# biz = [[0] * n for _ in range(n)]
biz = []
for i in range(m):
    r, c = map(int, input().split())
    # biz[r-1][c-1] = 1
    biz.append((r-1, c-1)) 


dx = [-1,1,0,0]
dy = [0,0,-1,1]

def isin(a, b):
    return 0<=a<n and 0<=b<n


                
def next_biz(x, y):
    Max = -1
    npos = (x, y)
    for dir in range(4):
        nx = x + dx[dir]
        ny = y + dy[dir]
        if isin(nx, ny) and arr[nx][ny] > Max:
            Max = arr[nx][ny]
            npos = (nx, ny)
    return npos

for i in range(t):
    nextpos = {}
    for x, y in biz:
        nx, ny = next_biz(x, y)
        if (nx, ny) in nextpos:
            nextpos[(nx, ny)].append((x, y))
        else:
            nextpos[(nx, ny)] = [(x, y)]

    newpos = []
    for now, prev in nextpos.items():
        if len(prev) == 1:
            newpos.append(now)
    
    biz = newpos

print(len(biz))