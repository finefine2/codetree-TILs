# simulation -> 시키는 대로 
# 같은값 n개이상 블럭 묶기 (bfs) 
K,M = tuple(map(int,input().split()))
board = [list(map(int,input().split())) for _ in range(5)] 
lst = list(map(int,input().split()))
ans = [] 
from collections import deque 
def bfs(board,v,sr,sc,clr): 
    q = deque()
    sset = set() 
    cnt = 0 

    q.append((sr,sc)) 
    v[sr][sc] = 1 

    sset.add((sr,sc)) 
    cnt += 1 
    while q: 
        cr,cc = q.popleft() 
        # 4방향 미방문 범위내 조건: 같은 값 
        for dr,dc in ((1,0),(0,1),(-1,0),(0,-1)): 
            nr,nc = cr + dr, cc + dc 
            if 0<=nr<5 and 0<=nc<5 and v[nr][nc] == 0 and board[cr][cc] == board[nr][nc]: 
                q.append((nr,nc)) 
                v[nr][nc] = 1 
                sset.add((nr,nc)) 
                cnt += 1 
    if cnt >= 3: # 유물이면 cnt 리턴, + clr == 1이면 0으로 clear 
        if clr == 1: 
            for r,c in sset: 
                board[r][c] = 0 
        return cnt 
    else: # 3개 미만이면 0 리턴 
        return 0 

def count_clear(board,clr): # clr = 1인 경우 3개 이상의 값들을 0으로 clear 
    v = [[0] * 5 for _ in range(5)] 
    cnt = 0 
    for r in range(5): 
        for c in range(5): # 미방문의 경우 같은 값이면 fill
            if v[r][c] == 0: 
                # 같은 값이면, 3개 이상인 경우 
                t = bfs(board,v,r,c,clr) 
                cnt += t 
    return cnt 

def rotate(arr,sr,sc): 
    narr = [x[:] for x in arr] 

    for r in range(3): 
        for c in range(3): 
            narr[sr+r][sc+c] = arr[sr+3-c-1][sc+r] 
    return narr 
# 총 K턴을 진행( 유물 없어지면 즉시 아웃) 
for _ in range(K): 
    # 1 탐사 진행 
    mx_cnt = 0 
    for rot in range(1,4): # 회전수 -> 열 -> 행 (작은순) 
        for sr in range(3): 
            for sc in range(3): 
                # rot 횟수만큼 90 도 시계방향 회전 nboard 
                nboard = [x[:] for x in board] 
                for _ in range(rot): 
                    nboard = rotate(nboard,sr,sc) 
                # 유물 갯수 카운팅 
                t = count_clear(nboard,0) 
                if t > mx_cnt: 
                    mx_cnt = t 
                    mboard = nboard
    # 유물이 없어지면 즉시종료 
    if mx_cnt == 0: 
        break 
    # 2 연쇄획득 
    board = mboard
    cnt = 0 
    while True: 
        t = count_clear(board,1) 
        if t == 0: #연쇄획득 종료 -> 다음 턴으로  
            break 
        cnt += t 

        # board 의 0값인 부분 리스트에서 순서대로 추가하기
        for c in range(5):
            for r in range(4,-1,-1): 
                if board[r][c] == 0: 
                    board[r][c] = lst.pop(0) 
    ans.append(cnt) # 이번 턴 연쇄획득한 갯수 추가 
for a in ans: 
    print(a,end=" ")