N = int(input()) 
OFFSET = 100
squares = [[0] * 201 for _ in range(201)] 
cnt = 0
for _ in range(N): 
    x1,y1,x2,y2 = map(int,input().split())
    x1,y1,x2,y2 = x1+OFFSET,y1+OFFSET,x2+OFFSET,y2+OFFSET
    for i in range(x1,x2):
        for j in range(y1,y2): 
            squares[i][j] = 1 

for i in range(201): 
    for j in range(201): 
        if squares[i][j] == 1: 
            cnt += 1
print(cnt)