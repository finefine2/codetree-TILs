# 겹치는 영역 + 연쇄처리를 위한 bfs 활용법
#방향: 상 우 하 좌
drs,dcs = [-1,0,1,0],[0,1,0,-1]

N,M,Q = tuple(map(int,input().split()))
# 벽으로 둘러싸서, 범위체크 안하고 범위밖으로 밀리지 않게 처리
board = [[2] * (N+2)] + [[2] + list(map(int,input().split())) + [2] for _ in range(N)] + [[2] * (N+2)]
units = {}

init_k = [0] * (M+1)
for m in range(1,M+1):
    sr,sc,h,w,k = tuple(map(int,input().split()))
    units[m] = [sr,sc,h,w,k]
    init_k[m] = k # 정답용 초기 체력 저장
def push_unit(start,dr): # s를 밀고, 연쇄처리
    q = []        #push 후보를 저장
    pset = set()  # 이동 기사번호를 저장
    damage = [0] * (M+1) # 각 유닛별 데미지 누적

    q.append(start) # 초기데이터 append
    pset.add(start)
    while q:
        cur = q.pop(0) # q에서 한개 꺼냄
        cr,cc,h,w,k = units[cur]

        # 명령받은 방향으로 진행, 벽이 아니면, 겹치는 다른조각이면 -> 큐에 삽입
        nr,nc = cr + drs[dr], cc + dcs[dr]
        for r in range(nr,nr+h):
            for c in range(nc,nc+w):
                if board[r][c] == 2:
                    #벽이면 모두 취소
                    return
                if board[r][c] == 1:
                    #함정인 경우
                    damage[cur] += 1 # 데미지 누적
        # 겹치는 다른 유닛이 있는 경우 큐에 추가 (모든 유닛을 체크)
        for idx in units:
            if idx in pset: continue # 이미 움직일 대상이면 체크할 필요 없음
            tr,tc,th,tw,tk = units[idx]

            # 겹치는 경우
            if nr<=tr+th-1 and tr <= nr+h-1 and tc <= nc+w-1 and nc <= tc+tw-1:
                q.append(idx)
                pset.add(idx)
    # 명령 받은 기사는 데미지 입지 않음
    damage[start] = 0

    # 이동, 데미지가 체력 이상이면 삭제처리
    for idx in pset:
        sr,sc,h,w,k = units[idx]
        if damage[idx] >= k:
            units.pop(idx)
        else:
            nr,nc = sr + drs[dr], sc + dcs[dr]
            units[idx] = [nr,nc,h,w,k-damage[idx]]

for _ in range(Q):
    idx,dr = tuple(map(int,input().split()))
    if idx in units:
        push_unit(idx,dr)
ans = 0
for idx in units:
    ans += init_k[idx] - units[idx][4]
print(ans)