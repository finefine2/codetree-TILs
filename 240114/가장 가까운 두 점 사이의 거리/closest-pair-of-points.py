'''
my solution 
'''
# N = int(input()) 
# points = [tuple(map(int,input().split())) for _ in range(N)] 

# ans = 1e9 
# for i in range(N): 
#     for j in range(i+1,N): 
#         r1,c1 = points[i][0], points[i][1] 
#         r2,c2 = points[j][0], points[j][1] 
#         tmp = ((r1-r2) * (r1-r2)) + ((c1-c2) * (c1-c2))
#         ans = min(ans, tmp)
# print(ans) 
import sys 
INT_MAX = sys.maxsize 
N = int(input()) 
points = [tuple(map(int,input().split())) for _ in range(N)]

def dist(i,j): 
    r1,c1 = points[i]
    r2,c2 = points[j] 
    return (r1-r2) * (r1-r2) + (c1-c2) * (c1-c2) 
min_dist = INT_MAX
for i in range(N): 
    for j in range(i+1,N): 
        min_dist = min(min_dist,dist(i,j)) 
print(min_dist)