# 맞았는데 살짝씩 오류?
# OFFSET = 2000 
# MAX_R = 2 * OFFSET + 1 

# rects = [[0] * MAX_R for _ in range(MAX_R)]

# for i in range(2): 
#     x1,y1,x2,y2 = map(int,input().split())
#     x1,y1,x2,y2 = x1+OFFSET,y1+OFFSET,x2+OFFSET,y2+OFFSET
#     for j in range(x1,x2):
#         for k in range(y1,y2): 
#             rects[j][k] = i + 1 
# cnt = []
# ans = 0 
# for i in range(MAX_R): 
#     for j in range(MAX_R): 
#         if rects[i][j] == 1: 
#             cnt.append([i,j]) 
#             ans += 1

# min_x = 10000
# max_x = -10000 
# min_y = 10000
# max_y = -10000 
# if cnt == []:
#     print(0) 
# else:
#     for x,y in cnt: 
#         min_x = min(x,min_x) 
#         max_x = max(x,max_x) 
#         min_y = min(y,min_y) 
#         max_y = max(y,max_y)
#     print((max_x-min_x+1) * (max_y-min_y+1))

OFFSET = 1000
MAX_R = 2 * OFFSET

n = 2 
rects = [ map(int,input().split()) for _ in range(n)]

checked = [[0] * (MAX_R + 1) for _ in range(MAX_R+1)]

for i, (x1,y1,x2,y2) in enumerate(rects, start=1): 
    x1,y1 = x1 + OFFSET, y1 + OFFSET
    x2,y2 = x2 + OFFSET, y2 + OFFSET

    # 직사각형에 주어진 순으로 1,2 번호를 붙임 
    for x in range(x1,x2): 
        for y in range(y1,y2): 
            checked[x][y] = i 

# 1,2 순으로 입력했는데도 아직 숫자 1로 남아있는 영역의 최대 최소 x,y 좌표를 계산 
min_x, max_x, min_y, max_y = MAX_R, 0, MAX_R, 0 
first_rect_exist = False 

for x in range(MAX_R + 1): 
    for y in range(MAX_R + 1): 
        if checked[x][y] == 1: 
            first_rect_exist = True 
            min_x = min(min_x, x) 
            max_x = max(max_x, x) 
            min_y = min(min_y, y) 
            max_y = max(max_y, y) 

# 넓이 계산 
if not first_rect_exist: 
    area = 0 
else: 
    area = (max_x - min_x + 1) * (max_y - min_y + 1) 
print(area)