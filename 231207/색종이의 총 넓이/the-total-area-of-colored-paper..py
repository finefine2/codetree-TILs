OFFSET = 100 
MAX_R = 2 * OFFSET + 1 

squares = [[0] * MAX_R for _ in range(MAX_R)] 
N = int(input())

for _ in range(N):
    x1,y1 = map(int,input().split())

    x1,y1 = x1+OFFSET,y1+OFFSET

    for i in range(x1,x1+8): 
        for j in range(y1,y1+8): 
            squares[i][j] = 1 
ans = 0 
for i in range(MAX_R): 
    for j in range(MAX_R): 
        if squares[i][j] == 1: 
            ans += 1
print(ans)