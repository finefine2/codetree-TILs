# N, K = map(int,input().split()) 
# placed = [0] * 100

# for _ in range(N): 
#     c, p = map(int,input().split()) 
#     # 여러 바구니가 한 지점에 있을 수 있음
#     placed[p-1] += c 
# ans = -5000

# # 구간 설정 함수 
# for i in range(100):
#     start = max(0,i-K) 
#     end = min(100,i+K+1)
#     ans = max(ans,sum(placed[start:end]))
# print(ans) 

# given solution 
# 모든 구간의 시작점을 정하고 완탐. 중심을 기준으로 c-K, c+K 구간에 존재하는 바구니가 주어진 위치를 넘지 않도록 
# 가능한 모든 구간을 완탐 돌리는데, 각 점마다 정해진 범위 내에 존재하는지 체크 
MAX_NUM = 100

N,K = map(int,input().split()) 
placed = [0] * (MAX_NUM+1) 
for _ in range(N): 
    c, p = map(int,input().split()) 
    placed[p] += c 
# 모든 구간의 시작점 체크 
max_sum = 0 
for i in range(MAX_NUM): 
    # 해당 구간 원소의 합 
    sum_all = 0 
    for j in range(i-K,i+K+1): 
        if 0 <= j <= MAX_NUM: 
            sum_all += placed[j] 
    max_sum = max(max_sum, sum_all) 
print(max_sum)