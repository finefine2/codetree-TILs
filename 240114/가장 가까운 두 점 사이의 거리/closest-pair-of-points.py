# # 두 개를 정하는 탐색 
# for i in range(N): 
#     for j in range(i+1,N): 
#         for k in range(N): 
#             if k == i or k == j: 
#                 continue 
#             x1,x2 = lines[k] 
#             for l in range(x1,x2+1): 
#                 count[l] += 1 
#         max_cnt = max(count) 
#         ans = min(ans,max_cnt) 
# print(ans) 

N = int(input()) 
points = [tuple(map(int,input().split())) for _ in range(N)] 

ans = 1e9 
for i in range(N): 
    for j in range(i+1,N): 
        r1,c1 = points[i][0], points[i][1] 
        r2,c2 = points[j][0], points[j][1] 
        tmp = ((r1-r2) * (r1-r2)) + ((c1-c2) * (c1-c2))
        ans = min(ans, tmp)
print(ans)