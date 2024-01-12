st = input()

x, y = 0,0
dx = [0,1,-1,0]
dy = [1,0,0,-1]

i = 0
for k in st:
    if k == 'L':
        i -= 1
        # x += dx[(i-1) % 3] 
        # y += dy[(i-1) % 3]
    elif k == 'R':
        i += 1
        # x += dx[(i+1) % 3]
        # y += dx[(i+1) % 3]
    elif k == 'F':
        x += dx[i % 3]
        y += dy[i % 3]

print(x, y)