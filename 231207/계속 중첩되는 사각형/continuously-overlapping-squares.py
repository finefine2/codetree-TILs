n = int(input()) 
# 빨, 파, 빨, 파 
# 홀 짝 홀 짝 
# 짝수 색들의 영역을 구한다 
OFFSET = 100 
MAX_R = 2 * OFFSET + 1 
rects = [[0] * MAX_R for _ in range(MAX_R)]

for i in range(n): 
    x1,y1,x2,y2 = map(int,input().split()) 

    for r in range(x1,x2): 
        for c in range(y1,y2): 
            rects[r][c] = i + 1 
cnt = 0 

for i in range(MAX_R): 
    for j in range(MAX_R): 
        if rects[i][j] > 0 and rects[i][j] % 2 == 0: 
            cnt += 1
print(cnt)