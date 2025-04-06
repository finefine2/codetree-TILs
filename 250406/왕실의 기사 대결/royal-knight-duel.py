drs,dcs = [-1,0,1,0],[0,1,0,-1]

L,N,Q = map(int,input().split())
board = [[2] * (L+2)] + [[2] + list(map(int,input().split())) + [2] for _ in range(L)] + [[2] * (L+2)]

knights = {}
init_k = [0] * (N+1)
for n in range(1,N+1):
    r,c,h,w,k = map(int,input().split())
    knights[n] = [r,c,h,w,k]
    init_k[n] = k

from collections import deque 

def push_unit(start,d): 
    q = deque() 
    pset = set() 
    
    damage = [0] * (N+1)
    pset.add(start)
    q.append(start) 
    
    while q: 
        cur = q.popleft() 
        cr,cc,h,w,k = knights[cur] 
        
        nr,nc = cr + drs[d], cc + dcs[d]
        # 벽이나 함정 체크
        for r in range(nr,nr+h): 
            for c in range(nc,nc+w): 
                if board[r][c] == 2: 
                    return 
                if board[r][c] == 1: 
                    damage[cur] += 1
                    
        # 다른 기사와의 충돌 체크
        for idx in knights: 
            if idx in pset: continue
            tr,tc,th,tw,tk = knights[idx] 
            
            # 충돌 판정 수정
            if nr <= tr + th - 1 and nr + h -1 >= tr and nc <= tc + tw -1 and nc + w -1 >= tc: 
                pset.add(idx) 
                q.append(idx) 
    
    # 명령을 받은 기사는 데미지를 입지 않음
    damage[start] = 0
    
    # 기사들의 상태 갱신
    can_move = True
    for idx in pset: 
        sr,sc,h,w,k = knights[idx] 
        
        if damage[idx] >= k: 
            knights.pop(idx)
            if idx == start:
                can_move = False
                break
    
    # 모든 기사가 이동 가능한 경우에만 이동
    if can_move:
        for idx in pset:
            if idx in knights:  # 생존한 기사만 이동
                sr,sc,h,w,k = knights[idx] 
                nr,nc = sr + drs[d], sc + dcs[d] 
                knights[idx] = [nr,nc,h,w,k-damage[idx]]

# 명령 수행
for _ in range(Q):
    idx,d = map(int,input().split())
    if idx in knights:
        push_unit(idx,d)

# 총 데미지 계산
ans = 0
for i in range(1, N+1):
    if i in knights:
        ans += init_k[i] - knights[i][4]
print(ans)