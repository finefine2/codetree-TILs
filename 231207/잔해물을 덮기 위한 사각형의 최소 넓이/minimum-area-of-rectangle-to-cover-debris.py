OFFSET = 2000 
MAX_R = 2 * OFFSET + 1 

rects = [[0] * MAX_R for _ in range(MAX_R)]

for i in range(2): 
    x1,y1,x2,y2 = map(int,input().split())
    x1,y1,x2,y2 = x1+OFFSET,y1+OFFSET,x2+OFFSET,y2+OFFSET
    for j in range(x1,x2+1):
        for k in range(y1,y2+1): 
            rects[j][k] = i + 1 
cnt = []
ans = 0 
for i in range(MAX_R): 
    for j in range(MAX_R): 
        if rects[i][j] == 1: 
            cnt.append([i,j]) 
            ans += 1

min_x = 10000
max_x = -10000 
min_y = 10000
max_y = -10000 
if cnt == []:
    print(0) 
else:
    for x,y in cnt: 
        min_x = min(x,min_x) 
        max_x = max(x,max_x) 
        min_y = min(y,min_y) 
        max_y = max(y,max_y)
    print((max_x-min_x) * (max_y-min_y))