n = int(input())
dx = [1,0,-1,0]
dy = [0,1,0,-1]
x , y = 0, 0
for i in range(n):
    a, b = map(str, input().split())
    b = int(b)
    if a == 'N':
        for j in range(b):
            x += dx[1] 
            y += dy[1]
    if a == 'S':
        for j in range(b):
            x += dx[3] 
            y += dy[3]
    if a == 'W':
        for j in range(b):
            x += dx[2] 
            y += dy[2]
    if a == 'E':
        for j in range(b):
            x += dx[0] 
            y += dy[0]

print(x, y)