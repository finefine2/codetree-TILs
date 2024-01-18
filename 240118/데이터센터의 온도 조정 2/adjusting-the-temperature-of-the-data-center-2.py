# max_score = 0 

# def get_score_a(num): 
#     if num < 10: 
#         return 5 
#     elif num < 20: 
#         return 8 
#     else: 
#         return 10 

# def get_score_b(num): 
#     if num < 6: 
#         return 12 
#     elif num < 15: 
#         return 10 
#     else: 
#         return 6 
# for i in range(0,31): 
#     score_a = get_score_a(i) 
#     score_b = get_score_b(i) 
#     max_score = max(max_score,score_a + score_b) 
# print(max_score)

N,C,G,H = map(int,input().split()) 
temps = [] 
for i in range(N): 
    Ta, Tb = map(int,input().split()) 
    temps.append([Ta,Tb]) 

def get_score(num,ta,tb): 
    global C,G,H
    if num < ta: 
        return C 
    elif ta <= num < tb: 
        return G 
    else: 
        return H 

def sum_score(num,temps): 
    ans = 0 
    for t in temps: 
        ans += get_score(num,t[0],t[1])
    return ans 
# 온도 i를 이용해서 완전탐색 돌리자 
# score 계산의 경우 모든 장비에 대해서 전부 진행해야 하는 것
max_score = 0 
for i in range(0,1001): 
    tmp = sum_score(i,temps) 
    max_score = max(tmp,max_score)
print(max_score)