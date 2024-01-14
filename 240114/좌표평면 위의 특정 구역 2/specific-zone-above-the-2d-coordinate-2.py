'''
생각보다 좌표 간 거리차이가 커질 수 있으므로 최댓값을 낭낭하게
sys.maxsize
'''
# N = int(input()) 

# ans = 1e12
# points = [] 
# for _ in range(N): 
#     r,c = map(int,input().split()) 
#     points.append([r,c]) 

# for i in range(N): 
#     min_r, min_c = 50000,50000
#     max_r, max_c = 0,0
#     for j in range(N): 
#         if j == i: 
#             continue
        
#         r,c = points[j][0], points[j][1] 
#         min_r = min(min_r,r) 
#         min_c = min(min_c,c) 
#         max_r = max(max_r,r) 
#         max_c = max(max_c,c) 

#     ans = min(ans, abs(max_r-min_r) * abs(max_c-min_c))
# print(ans)

'''
given solution 
어떤 점을 제외해야 최소 넓이가 될 지 생각하는 것은 골치아프기에, 모든 점을 다 제외시켜보며 
남은 N-1개 점들에 대해 최소 사각형 넓이를 구해 그 중 최솟값을 구한다 
'''

import sys 
INT_MAX = sys.maxsize
N = int(input()) 
points = [tuple(map(int,input().split())) for _ in range(N)] 

ans = INT_MAX
# 빼야하는 점을 선택 
for i in range(N): 
    # i번 점을 제외한 나머지 점들을 포함하기 위한 최소 넓이 계산 
    # 최소 넓이 = 남은 점들의 x 좌표 중 최소, 최대 y 좌표 중 최소 최대 
    min_x, max_x = INT_MAX, 1 
    min_y, max_y = INT_MAX, 1 
    for j, (x,y) in enumerate(points): 
        # i번 점은 패스
        if j == i: 
            continue
        min_x = min(min_x,x) 
        max_x = max(max_x,x) 
        min_y = min(min_y,y) 
        max_y = max(max_y,y) 
    ans = min(ans, (max_x - min_x) * (max_y - min_y))
print(ans)