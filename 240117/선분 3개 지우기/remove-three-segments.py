'''
my solution 
일단 전부 골라보자 
n-3 개 선분들을 전부 고른다
그리고 겹치는지 안 겹치는지 체크한다 
'''
# N = int(input()) 
# lines = [tuple(map(int,input().split())) for _ in range(N)] 

# def check_overlap(a,b,c): 
#     count = [0] * 101
#     ans = True
#     for i in range(N): 
#         if i in [a,b,c]: 
#             continue
#         x1, x2 = lines[i] 
#         # print(i)
#         # print(x1,x2) 
#         for j in range(x1,x2+1): 
#             count[j] += 1
#         # print(count) 
#         if 2 not in count: 
#             ans = True 
#         else: 
#             ans = False 
#             break 
              
#     return ans 

# ans = 0
# for i in range(N): 
#     for j in range(i+1,N): 
#         for k in range(j+1,N): 
#             if check_overlap(i,j,k): 
#                 ans += 1 
# print(ans)  

'''
given solution
선분들이 할당되는 포인트마다 count 배열에 +1 씩 하고, count가 2 이상이면 선분이 겹친 것이므로 세지 않음 
'''
MAX_L = 100 
N = int(input())
lines = [tuple(map(int,input().split())) for _ in range(N)]

# 3개 선분을 모두 골라 겹치지 않는 가짓수 카운팅 
ans = 0 
for i in range(N): 
    for j in range(i+1,N): 
        for k in range(j+1,N): 
            # i,j,k 를 제외 시 모든 선분이 겹치지 않으면 1 추가 
            # overlap: 모든 선분이 안 겹치면 false 
            overlap = False 
            count = [0] * (MAX_L+1) 
            for x in range(N): 
                # 제외한 3개 선분이면 패스 
                if x == i or x == j or x == k: 
                    continue
                for y in range(lines[x][0], lines[x][1] + 1): 
                    count[y] += 1
            for x in range(MAX_L+1): 
                if count[x] > 1: 
                    overlap = True 
            if overlap == False: 
                ans += 1 
print(ans)