'''
my solution - 함수 모듈화를 이용한 풀이 
'''
# N,C,G,H = map(int,input().split()) 
# temps = [] 
# for i in range(N): 
#     Ta, Tb = map(int,input().split()) 
#     temps.append([Ta,Tb]) 

# def get_score(num,ta,tb): 
#     global C,G,H
#     if num < ta: 
#         return C 
#     elif ta <= num <= tb: 
#         return G 
#     else: 
#         return H 

# def sum_score(num,temps): 
#     ans = 0 
#     for t in temps: 
#         ans += get_score(num,t[0],t[1])
#     return ans 
# # 온도 i를 이용해서 완전탐색 돌리자 
# # score 계산의 경우 모든 장비에 대해서 전부 진행해야 하는 것
# max_score = 0 
# for i in range(0,1001): 
#     tmp = sum_score(i,temps) 
#     max_score = max(tmp,max_score)
# print(max_score)

'''
given sol 
복잡할 땐 함수 모듈화를 통해서 진행하자 
온도가 주어질 때 각 장비 작업량의 합을 구하기 위해, 
장비마다 특정 온도에서 작업량을 계산 후 합하기 
'''
MAX_T = 1000
N,C,G,H = map(int,input().split()) 
ta,tb = [0] * N, [0] * N 
for i in range(N): 
    ta[i], tb[i] = map(int,input().split()) 
# 특정 장비의 t온도에서의 작업량 
def single_efficiency(low,high,t): 
    global C,G,H 
    c,g,h = C,G,H
    if t < low: 
        return c 
    elif t <= high: 
        return g 
    else: 
        return h 
# t온도에서의 작업량 
def performance(t): 
    total_efficiency = 0 
    # 장비별 작업량의 합 계산 
    for i in range(N): 
        total_efficiency += single_efficiency(ta[i],tb[i],t) 
    return total_efficiency 
max_score = 0 
for t in range(MAX_T+1): 
    max_score = max(max_score, performance(t)) 
print(max_score)