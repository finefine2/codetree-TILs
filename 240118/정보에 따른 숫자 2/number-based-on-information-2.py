'''
my solution 
'''
# T, a, b = map(int,input().split()) 
# pos = [] 
# for _ in range(T): 
#     c,x = input().split()
#     pos.append([c,int(x)]) 

# # 매 위치를 갱신하면서 체크하기 
# def check_dist(pos,num): 
#     dist1 = 10000 
#     dist2 = 10000
#     for c,x in pos: 
#         if c == "S": 
#             dist1 = min(dist1, abs(num-x))
#         elif c == "N": 
#             dist2 = min(dist2, abs(num-x)) 
#     if dist1 <= dist2: 
#         return True 
# ans = 0 
# for i in range(a,b+1): 
#     if check_dist(pos,i):
#         ans += 1 
# print(ans) 

'''
given solution 
S와 N 위치를 배열에 저장하고, a~b 사이 숫자들에 대해 모든 수에 대해 S N 중 어디에 더 가까운지 완탐 
모든 S N 까지 거리 구하고 작은 것 고르기 
'''
import sys 
INT_MAX = sys.maxsize 
t,a,b = map(int,input().split()) 
sn_data = [tuple(input().split()) for _ in range(t)] 
ans = 0 
# 각 수에 대해 s에 가까운지 n에 가까운지 판단 
for i in range(a,b+1): 
    dist_s, dist_n = INT_MAX, INT_MAX
    for p,q in sn_data: 
        q = int(q) 
        if p == "S": 
            dist_s = min(dist_s, abs(q-i)) 
        else: 
            dist_n = min(dist_n, abs(q-i)) 
    if dist_s <= dist_n: 
        ans += 1
print(ans)