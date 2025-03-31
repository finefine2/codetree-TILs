'''
복잡한 문제 -> 단계별 구현/검증
문제를 전체적으로 이해하고 단계별로 나눠서 구현하고 검증하기

[1] 메두사의 이동: 도로를 따라 공원까지 최단경로 (상하좌우) 이동한 칸에 전사가 있으면 전사 사라짐
[2] 메두사의 시선(상하좌우): 가장 많이 돌로 만드는 방향
8방향 중에 한 방향에 전사가 위치하면, 그 전사가 동일한 방향으로 바라본 범위 칸은 안 보임
[3]전사들의 이동(메두사 쪽)
- 첫번쨰: 상하좌우 이동
- 두번째: 좌우상하 이동
[4] 전사 공격: 공격 후 사라짐
'''

# [0] BFS 이동경로 저장 상하좌우
# route [[1,2],11 21 22 31 31]
'''
for mi,mj in route: 
1] 전사좌표 == mi,mj -> 삭제

2] 메두사 시선: 가장 많이 돌로 만들 수 있는 방향
v, stone 

3] 전사들의 이동
men = [] 


'''
from collections import deque
def find_route(sr,sc,er,ec):
    q = deque()
    v = [[0] * N for _ in range(N)]

    q.append((sr,sc))
    v[sr][sc] = ((sr,sc)) # 출발지점, 직전위치를 저장

    while q:
        cr,cc = q.popleft()

        if (cr,cc) == (er,ec): # 목적지 도착! 경로 저장
            route = []
            cr,cc = v[cr][cc]
            while (cr,cc) != (sr,sc): #출발지가 아니라면 저장
                route.append((cr,cc))
                cr,cc = v[cr][cc]
            return route[::-1]    # 역순 (메두사 이동순서대로)

        # 4방향 (상하좌우!) 범위내 미방문 조건 (==0)
        for dr,dc in ((-1,0),(1,0),(0,-1),(0,1)):
            nr,nc = cr + dr, cc + dc
            if 0<=nr<N and 0<=nc<N and v[nr][nc] == 0 and arr[nr][nc] == 0:
                q.append((nr,nc))
                v[nr][nc] = (cr,cc)
    # 이곳까지 왔다는 얘기는? 목적지 못찾음
    return -1


def mark_line(v,cr,cc,dr):
    while 0<=cr<N and 0<=cc<N:
        v[cr][cc] = 2
        cr,cc = cr +drs[dr],cc+dcs[dr]
def mark_safe(v, si, sj, dr, org_dr):
    # [1] 직선방향 표시
    ci,cj = si+drs[dr], sj+dcs[dr]
    mark_line(v, ci, cj, dr)        # v에 dr방향으로 이동가능지역 표시

    # [2] 바라보는 방향으로 한줄씩 표시
    ci,cj = si+drs[org_dr],sj+dcs[org_dr]
    while 0<=ci<N and 0<=cj<N:          # 범위내라면 계속 진행
        mark_line(v, ci, cj, dr)        # v에 dr방향으로 이동가능지역 표시
        ci,cj = ci+drs[org_dr],cj+dcs[org_dr]

# tv,tstone = make_stone(marr,mr,mc,dr)
def make_stone(marr,mr,mc,dr):
    v = [[0]*N for _ in range(N)]
    cnt = 0
    # [1] dr 방향으로 >0 만날때까지 1표시, 이후 좌표 2표시
    nr,nc = mr + drs[dr], mc+dcs[dr]
    while 0<=nr<N and 0<=nc<N:
        v[nr][nc] = 1
        if marr[nr][nc] > 0:
            cnt += marr[nr][nc]
            nr,nc = nr + drs[dr], nc + dcs[dr]
            mark_line(v,nr,nc,dr)
            break
        nr,nc = nr + drs[dr], nc + dcs[dr]

    # [2] dr-1,dr+1 방향으로 동일처리, 대각선 원점잡고 dr방향
    for org_dr in ((dr-1) % 8, (dr+1) % 8):
        sr,sc = mr + drs[org_dr], mc + dcs[org_dr]
        while 0<=sr<N and 0<=sc<N:
            if v[sr][sc] == 0 and marr[sr][sc] > 0:
                v[sr][sc] = 1
                cnt += marr[sr][sc]
                mark_safe(v,sr,sc,dr,org_dr)
                break
            cr,cc = sr,sc
            while 0<=cr<N and 0<=cc<N:
                if v[cr][cc] == 0:
                    v[cr][cc] =1
                    if marr[cr][cc] > 0:
                        cnt += marr[cr][cc]
                        mark_safe(v,cr,cc,dr,org_dr)
                        break
                else:
                    break
                cr,cc = cr + drs[dr], cc + dcs[dr]
            sr,sc = sr + drs[org_dr], sc + dcs[org_dr]
    return v,cnt

# move_cnt, attk_cnt = move_men(v,mr,mc)
def move_men(v,mr,mc):
    move,attk = 0,0
    for dirs in (((-1,0),(1,0),(0,-1),(0,1)), ((0,-1),(0,1),(-1,0),(1,0))):
        for idx in range(len(men)-1,-1,-1):
            cr,cc = men[idx]
            if v[cr][cc] == 1:
                continue
            dist = abs(mr-cr) + abs(mc-cc)
            for dr,dc in dirs:
                nr,nc = cr + dr, cc + dc
                if 0<=nr<N and 0<=nc<N and v[nr][nc] != 1 and dist > abs(mr-nr) + abs(mc-nc):
                    if (nr,nc) == (mr,mc):
                        attk += 1
                        men.pop(idx)
                    else:
                        men[idx] = [nr,nc]
                    move += 1
                    break
    return move, attk
#######################
#######################

N,M = map(int,input().split())
sr,sc,er,ec = map(int,input().split())
tlst = list(map(int,input().split()))
men = []

for i in range(0,M*2,2):
    men.append([tlst[i],tlst[i+1]])
arr = [list(map(int,input().split())) for _ in range(N)]

#[0] BFS로 메두사 최단경로: 도로따라 공원까지 (여러개면 상하좌우) 없으면 -1
route = find_route(sr,sc,er,ec)
# print(route)
if route == -1:
    print(-1)
else:
    for mr,mc in route:
        move_cnt,attk_cnt = 0,0
        # [1] 메두사의 이동: 지정된 최단거리로 이동 *(전사 마주치면 삭제)
        for i in range(len(men)-1,-1,-1):  # 삭제시 역순으로
            if men[i] == [mr,mc]: #같은 좌표면 삭제
                men.pop(i)

        # 8방향
        # 상, 우상, 우, 우하, 하, 좌하, 좌, 좌상
        drs = [-1,-1,0,1,1,1,0,-1]
        dcs = [0,1,1,1,0,-1,-1,-1]
        # [2] 메두사의 시선: 상하좌우 네 방향 가장 많이 돌로 만드는 쪽 찾기
        # => v[] 에 표시해서 이동시 참조 (메두사시선==1, 전사에 가려진 곳 == 2, 빈 땅 == 0)
        # marr[][]: 지도에 있는 전사수
        marr = [[0] * N for _ in range(N)]
        for tr,tc in men:
            marr[tr][tc] += 1

        mx_stone = -1
        v = []
        for dr in (0,4,6,2): # 상하좌우 순서로 처리
            tv,tstone = make_stone(marr,mr,mc,dr)
            if mx_stone < tstone:
                mx_stone = tstone
                v = tv


        # [3] 전사들의 이동(한 칸씩 두번): 메두사 있을 시 공격
        move_cnt, attk_cnt = move_men(v, mr, mc)
        print(move_cnt, mx_stone, attk_cnt)
    print(0)