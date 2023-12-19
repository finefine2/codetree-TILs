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

# N, K, P, T = map(int,input().split()) 
# # 최종감염 여부는 아래 리스트에 저장 
# infects = [0] * N 
# P = P-1 
# # 처음 정해진 녀석은 감염 상태로 확정 
# infects[P] = 1 

# orders = [] 
# for _ in range(T): 
#     # t 초에 x와 y가 악수를 한다 
#     t,x,y = map(int,input().split()) 
#     x,y = x-1, y-1 
#     orders.append([t,x,y]) 

# orders.sort(key = lambda x: x[0]) 

# # 전체 악수 횟수를 카운팅하면 안 되고 각각의 사람들별로 악수횟수를 카운팅해야?
# cnt_list = [K] * N
# for i in range(T): 
#     x,y = orders[i][1], orders[i][2] 
#     # 전염된 사람이 아닌 개발자가 전염자와 악수하면, 전염은 되지만 전염 가능 횟수는 줄어들지 않음 
#     if infects[x] == 1 and cnt_list[x] > 0:
#         if infects[y] == 0: 
#             infects[y] = 1 
#             cnt_list[x] -= 1 
#         elif infects[y] == 1: 
#             cnt_list[x] -= 1 
#             cnt_list[y] -= 1 
#     elif infects[y] == 1 and cnt_list[y] > 0: 
#         if infects[x] == 0: 
#             infects[x] = 1 
#             cnt_list[y] -= 1 
#         elif infects[x] == 1: 
#             cnt_list[x] -= 1 
#             cnt_list[y] -= 1 
# for i in infects: 
#     print(i,end="")

# given solution 
'''
각 사람이 악수한 시간과 악수한 두 사람의 번호를 클래스에 저장. 
배열의 시간을 오름차순으로 정렬 
각 시간별로 악수한 두사람이 감염됐는지 체크하고, 각각의 전염 가능 횟수가 유효하면 상대를 전염 
'''
# 클래스 선언
class Shake:
    def __init__(self, time, person1, person2):
        self.time, self.person1, self.person2 = time, person1, person2

# 변수 선언 및 입력
n, k, p, t = tuple(map(int, input().split()))	
shakes = []
for _ in range(t):
    time, person1, person2 = tuple(map(int, input().split()))
    shakes.append(Shake(time, person1, person2))

shake_num = [0] * (n + 1)
infected = [False] * (n + 1)

infected[p] = True

# Custom Comparator를 활용한 정렬
shakes.sort(key = lambda x: x.time)

# 각 악수 횟수를 세서,
# K번 초과로 악수를 했을 시 전염시키지 않습니다.
for shake in shakes:
	target1 = shake.person1
	target2 = shake.person2
	
	# 감염되어 있을 경우 악수 횟수를 증가시킵니다.
	if infected[target1]:
		shake_num[target1] += 1
	if infected[target2]:
		shake_num[target2] += 1
	
	# target1이 감염되어 있고 아직 K번 이하로 악수했다면 target2를 전염시킵니다.
	if shake_num[target1] <= k and infected[target1]:
		infected[target2] = True
	
	# target2가 감염되어 있고 아직 K번 이하로 악수했다면 target1을 전염시킵니다.
	if shake_num[target2] <= k and infected[target2]:
		infected[target1] = True
		
for i in range(1, n + 1):
	if infected[i]:
		print(1, end="")
	else:
		print(0, end="")