# 주위를 벽으로 둘러싸기
# 밀림: 명령받은 기사 다음위치 (범위) - 모든 기사 겹침체크 재귀? bfs? 고민해야
# -> 겹침: q 추가..?
# -> q에서 하나씩 빼서 처리
# 이동대상 pset <- set() 추가 + 대미지 처리

# 기사정보 (r,c,h,w,k) -> dictionary 활용
# units = {1: [1,2,2,1,5], 2:[]..}
# init_k = [0,5, ]

# q번의 명령 후 '생존'한 기사들이 받은 데미지의 총합
# 함수화?
# 벽만나면 return
# pset의 unit들 dir방향으로 한 칸 움직임 디버깅용으로 표기
from collections import deque
import sys
sys.stdin = open("input.txt","r")

# d 0 1 2 3
# N E S W
N,M,Q = tuple(map(int,input().split()))
# 벽으로 둘러싸서, 범위체크 안하고 범위밖으로 밀리지 않게
board = [[2]*(N+2)]+[[2]+list(map(int, input().split()))+[2] for _ in range(N)]+[[2]*(N+2)]
# 기사들을 담을 변수
units = {}
v = [[0] * (N+2) for _ in range(N+2)] # 기사 위치 디버깅용
init_k = [0] * (M+1)
for m in range(1,M+1):
    sr,sc,h,w,k = tuple(map(int,input().split()))
    units[m] = [sr,sc,h,w,k]
    init_k[m] = k  # 초기 체력 저장 (ans처리)
    for i in range(sr,sr+h): # 디버그용
        for j in range(sc,sc+w):
            v[i][j] = m
drs,dcs = [-1,0,1,0],[0,1,0,-1]
def push_unit(start,d):  # s를 밀고, 연쇄처리
    q = deque() # 밀 대상들을 q에 넣기!
    pset = set() # 이동 기사번호를 저장
    damage = [0] * (M+1) # 각 유닛별 데미지 누적
    q.append(start)  # 초기 데이터 append
    pset.add(start)
    while q:
        cur = q.popleft() # q에서 데이터 한 개 꺼냄
        cr,cc,h,w,k = units[cur] # 기사 정보 불러오기

        # 명령받은 방향, 벽이 아니면, 겹치는 다른 조각이면 -> q에 삽입
        nr,nc = cr + drs[d], cc + dcs[d]
        for r in range(nr, nr + h):
            for c in range(nc, nc + w):
                if board[r][c] == 2: # 벽인 경우는 놉
                    return
                if board[r][c] == 1: # 함정인 경우
                    damage[cur] += 1
        # 겹치는 다른 유닛이 있으면 큐에 추가 (모든 유닛 체크)
        for idx in units:
            if idx in pset: continue # 이미 움직일 대상이면 체크할 필요 없음

            tr,tc,th,tw,tk = units[idx]
            # 겹치는 경우?

            if nr <= tr+tc-1 and nr+h-1>=tr and tc<nc+w-1 and nc<=tc+tw-1:
            # 겹치는 거 일일이 상하좌우 비교하며 확인 - 제일 무식한 방법
                # 겹치는 부분을 살펴보고
                q.append(idx)
                pset.add(idx)
    # 명령 받은 기사는 데미지없음
    damage[start] = 0
    # 이동 데미지가 체력이상이면 삭제처리
    for idx in pset:
        sr,sc,h,w,k = units[idx]
        if k <= damage[idx]: # 체력보다 데미지가 더 커지면
            units.pop(idx)
        else:
            nr,nc = sr+drs[d],sc+dcs[d]
            units[idx] = [nr,nc,h,w,k-damage[idx]]


# 명령받고 처리
for _ in range(Q):
    idx, d = tuple(map(int,input().split()))
    if idx in units:
        push_unit(idx,d)  # 명령받은 기사(연쇄적으로 밀기: 벽이 없는 경우)

ans = 0
# 초기체력과의 차이를 비교하면 되겠네
for idx in units:
    ans += init_k[idx] - units[idx][4]
print(ans)