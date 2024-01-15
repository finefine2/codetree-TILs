n = int(input())

dx = [0,0,-1,1]
dy = [-1,1,0,0]

dir = {'W' : 0, 'E' : 1, 'N' : 2, 'S' : 3}
dir_num = 0

ans = 0
x, y = 0,0
t = 0
check = False
for i in range(n):
    a,b = map(str, input().split())
    
    dir_num = (dir[a]) % 4

    for j in range(int(b)):
        x = x + dx[dir_num]
        y = y + dy[dir_num]
        t += 1

        
        if x == 0 and y == 0:
            ans = t
            check = True

        if check:
            break

    if ans != 0:
        break

if ans == 0:
    print(-1)
else:
    print(ans)