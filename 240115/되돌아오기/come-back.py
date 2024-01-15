n = int(input())

dx = [0,0,-1,1]
dy = [-1,1,0,0]

dir = {'W' : 0, 'E' : 1, 'N' : 2, 'S' : 3}
dir_num = 0
arr = [[0] * (n*n) for _ in range(n*n)]

ans = 0
x, y = n,n
t = 0
for i in range(n):
    a,b = map(str, input().split())
    
    dir_num = dir[a]
    for j in range(int(b)):
        x = x + dx[dir_num]
        y = y + dy[dir_num]
        t += 1
        
        if x == n and y == n:
            ans = t
            break

if ans == 0:
    print(-1)
else:
    print(ans)