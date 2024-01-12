st = input()

x, y = 0,0
dx = [1,0,-1,0]
dy = [0,-1,0,1]

i = 3
for k in st:
    if k == 'L':
        i = (i + 3) % 4
        # x += dx[(i-1) % 3] 
        # y += dy[(i-1) % 3]
    elif k == 'R':
        i = (i + 1) % 4
        # x += dx[(i+1) % 3]
        # y += dx[(i+1) % 3]
    else:
        x += dx[i % 3]
        y += dy[i % 3]

print(x, y)