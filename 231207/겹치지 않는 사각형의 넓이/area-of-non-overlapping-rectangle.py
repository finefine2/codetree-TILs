OFFSET = 1000
MAX_R = 2 *OFFSET + 1

squares = [[0] * MAX_R for _ in range(MAX_R)]
for i in range(3): 
    x1,y1,x2,y2 = map(int,input().split())
    x1,y1,x2,y2 = x1+OFFSET, y1+OFFSET, x2+OFFSET, y2+OFFSET

    for j in range(x1,x2): 
        for k in range(y1,y2): 
            squares[j][k] = i + 1 
cnt = 0 
for i in range(MAX_R): 
    for j in range(MAX_R):
        if squares[i][j] == 1 or squares[i][j] == 2: 
            cnt += 1 
print(cnt)