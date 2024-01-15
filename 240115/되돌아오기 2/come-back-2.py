st = input()

dx = [-1,0,1,0]
dy = [0,-1,0,1]

ans = 0
x, y = 0,0
dir = 0
cnt = 0
for k in st:
    if k == 'L':
        dir = (dir + 1) % 4 
        cnt += 1
    elif k == 'R':
        dir = (dir - 1) % 4
        cnt += 1
    else:
        x += dx[dir]
        y += dy[dir]
        cnt += 1
    
    if x == 0 and y == 0:
        ans = cnt
        break

if ans == 0:
    print(-1)
else:
    print(ans)