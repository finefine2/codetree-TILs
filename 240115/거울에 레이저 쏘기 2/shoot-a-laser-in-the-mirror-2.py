n = int(input())

dx = [1,0,-1,0]
dy = [0,-1,0,1]

arr = []
for i in range(n):
    tmp = input()
    arr.append(tmp)

start = int(input())

def isin(a, b):
    return 0<=a<n and 0<=b<n

def move(x, y, dir):
    nx = x + dx[dir]
    ny = y + dy[dir]
    return nx, ny, dir

if start <= n:
    x = 0
    y = start - 1
    dir = 0
elif start <= 2 * n:
    x = start - n - 1
    y = n - 1
    dir = 1
elif start <= 3 * n:
    x = n - 1
    y = n - (start - 2 * n)
    dir = 2
else:
    x = n - (start - 3 * n)
    y = 0
    dir = 3

t = 0
while isin(x, y):
    if arr[x][y] == '/':
        x, y, dir = move(x, y, dir ^ 1)
    else:
        x, y, dir = move(x, y, 3 - dir)
    
    t += 1

print(t)