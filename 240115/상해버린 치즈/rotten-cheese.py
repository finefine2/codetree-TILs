# 모든 치즈에 대해 해당 치즈가 상했을 때의 완탐 
# 사람이 치즈를 먹지 않거나, 아프기 시작한 순간이 치즈 먹은 순간보다 빠르면 모순 

'''
각각의 치즈가 상했다고 가정했을 때 아플 수 있는 최대 인원 구하기 

각 사람이 가장 먼저 치즈 먹은 시간 저장하고, 저장한 값과 단서 비교시, 다음 2가지 모순 발생
모순이 발생하면 해당 치즈는 상할 수 없음
1. 단서로 주어진 아픈 사람이 치즈를 먹은 기록이 없으면 모순 
2. 아프기 시작한 순간이 치즈를 먹은 순간보다 빠르면 모순

그 외에는 전부 아플 가능성 존재하므로,약이 필요하다고 간주 
'''

# 변수를 여러 개 받을 때는 클래스를 선언하자 
class Info1: 
    def __init__(self,p,m,t): 
        self.p, self.m, self.t = p,m,t 
class Info2: 
    def __init__(self,p,t): 
        self.p, self.t = p,t 

# 변수 선언 및 입력 
N, M, D, S = map(int,input().split()) 
info1 = [] 
for _ in range(D): 
    p,x,t = map(int,input().split()) 
    info1.append(Info1(p,x,t)) 
info2 = [] 
for _ in range(S): 
    p,t = map(int,input().split()) 
    info2.append(Info2(p,t))
ans = 0 

# 치즈가 상했을 시 필요한 약의 최대 개수
for i in range(1, M+1): 
    # i 번째 치즈가 상했을 때 필요한 약의 개수
    # 치즈가 상했다고 가정하고 모순이 발생하는지 확인
    # time 배열 만들어 각자 언제 치즈 먹었는지 저장
    time = [0] * (N+1) 
    for info in info1: 
        #i 치즈가 아닌 경우 패스 
        if info.m != i: 
            continue 
        # i번째 치즈를 처음 먹었거나 이전보다 더 빨리 먹게 되면 time배열 갱신 
        person = info.p 
        if time[person] == 0: 
            time[person] = info.t 
        elif time[person] > info.t: 
            time[person] = info.t 
    # possible: i번째 치즈가 상할 수 있으면 true, 아니면 false 
    possible = True 

    for info in info2: 
        # i번째 치즈를 안 먹었거나 i번 치즈를 먹은 시간보다 먼저 아프면 모순 
        person = info.p 
        if time[person] == 0: 
            possible = False 
        if time[person] >= info.t: 
            possible = False 
    # i번 치즈가 상했다면, 몇 개 약이 필요한지 
    pill = 0 
    if possible: 
        # i번 치즈를 먹었다면, 약이 필요 
        for j in range(1,N+1): 
            if time[j] != 0: 
                pill += 1 
    ans = max(ans,pill) 
print(ans)