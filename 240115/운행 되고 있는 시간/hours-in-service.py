'''
my solution 
'''
# N = int(input())
# points = [tuple(map(int,input().split())) for _ in range(N)]
# ans = -1e9 

# for i in range(N): 
#     lines = [0] * 1001
#     for j in range(N): 
#         if j == i: 
#             continue
#         a,b = points[j] 
#         for k in range(a,b): 
#             lines[k] = 1
#     ans = max(ans,sum(lines))
# print(ans) 

'''
given solution 
한 명씩 제외하며 완탐 
운행 시간을 범위로 잡고, 하나의 범위를 제외하고 나머지 범위가 최대가 되도록
제외할 사람을 한 명씩 잡고, 나머지의 운행시간을 모두 구하기 
'''
MAX_NUM = 1000 
N = int(input()) 
lines = [tuple(map(int,input().split())) for _ in range(N)] 

ans = 0 
for i in range(N): 
    # i번 사람을 제외한 나머지 구간에서 운행시간을 구함 
    count = [0] * MAX_NUM
    for j,(l,r) in enumerate(lines): 
        if j == i: 
            continue
        for k in range(l,r): 
            count[k] += 1 
    time = 0 
    # 이 부분이 나랑 차이인듯 
    for j in range(1,MAX_NUM): 
        if count[j] > 0: 
            time += 1 
    ans = max(ans,time) 
print(ans)