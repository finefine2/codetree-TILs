# N 명 
# 전염시킬 수 있는 횟수 K번 
# 첫 감염자는 P
# T 악수에 대한 정보 
# 전염에 대한 조건?: 
'''
2번까지만 감염 시킬 수 있음 
1 2 3 4 

첫 감염자는 2번임 

7초에 1과 2 악수 

5초에 2와 3 악수 
3번 감염됨 --> 3번도 감염 

6초에 2와 4 악수 
4번과 2번 악수 --> 4번도 감염

최대 감염횟수 끝 

해야할 것 정리 
1. 시간에 따른 악수 order 정렬하기 
2. 악수 횟수 카운팅하기 악수횟수가 K번이 되면 끝 
'''

N, K, P, T = map(int,input().split()) 
# 최종감염 여부는 아래 리스트에 저장 
infects = [0] * N 
P = P-1 
# 처음 정해진 녀석은 감염 상태로 확정 
infects[P] = 1 

orders = [] 
for _ in range(T): 
    # t 초에 x와 y가 악수를 한다 
    t,x,y = map(int,input().split()) 
    x,y = x-1, y-1 
    orders.append([t,x,y]) 

orders.sort(key = lambda x: x[0]) 

# 전체 악수 횟수를 카운팅하면 안 되고 각각의 사람들별로 악수횟수를 카운팅해야?
cnt_list = [K] * N

for i in range(T): 
    x,y = orders[i][1], orders[i][2] 

    if infects[x] == 1 and cnt_list[x] > 0:
        infects[y] = 1 
        cnt_list[x] -= 1
        cnt_list[y] -= 1
    elif infects[y] == 1 and cnt_list[y] > 0: 
        infects[x] = 1 
        cnt_list[x] -= 1
        cnt_list[y] -= 1
for i in infects: 
    print(i,end="")