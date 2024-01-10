# N = 5 
# segments = [(1,3),(2,4),(5,8),(6,9),(7,10)]

# ans = 100 
# for i in range(N): 
#     count = [0] * 11 
#     for j in range(N): 
#         if j == i: 
#             continue 
#         x1,x2 = segments[j] 
#         for k in range(x1,x2+1): 
#             count[k] += 1  
#     max_cnt = max(count) 
#     ans = min(ans,max_cnt) 
# print(ans) 

N = int(input()) 

ans = 1e9 
points = [] 
for _ in range(N): 
    r,c = map(int,input().split()) 
    points.append([r,c]) 

for i in range(N): 
    min_r, min_c = 50000,50000
    max_r, max_c = 0,0
    for j in range(N): 
        if j == i: 
            continue
        
        r,c = points[j] 
        min_r = min(min_r,r) 
        min_c = min(min_c,c) 
        max_r = max(max_r,r) 
        max_c = max(max_c,c) 

    ans = min(ans, abs(max_r-min_r) * abs(max_c-min_c))
print(ans)