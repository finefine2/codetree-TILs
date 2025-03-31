'''
3차원, 2차원 나눠서 처리

경로 찾기 bfs?
시작좌표부터 나오는 곳까지 3차원 bfs처리라고 생각한다면

단계를 크게크게
top - down 으로 처리할 것
3차원 bfs 후에 2차원 bfs를 한다
bfs_3d: 평면간 이동을 고려한다
bfs_2d: (시간 이상) 벽 처리

[1] 3d, 2d 시작 / 종료 좌표 탐색

[2] bfs_3d (경로x -1)
평면간 이동

[3] bfs_2d
v[] 값보다 작을 때 확산


'''

N,M,F = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
# 3차원 평면 - 동서남북 윗면
arr3 = [[list(map(int,input().split())) for _ in range(M)] for _ in range(5)]
wall = [list(map(int,input().split())) for _ in range(F)]

def myprint_3d(arr3):
    for arr in arr3:
        for lst in arr:
            print(*lst)
        print()
    print()

def myprint_2d(arr):
    for lst in arr:
        print(*lst)
    print()
def find_3d_start():
    for r in range(M):
        for c in range(M):
            if arr3[4][r][c] == 2:
                return 4,r,c
def find_2d_end():
    for r in range(N):
        for c in range(N):
            if arr[r][c] == 4:
                arr[r][c] = 0
                return r,c

def find_3d_base():
    for r in range(N):
        for c in range(N):
            if arr[r][c] == 3:
                return r,c
def find_3d_end_2d_start():
    #[1] 3차원 시작좌표 찾기
    br,bc = find_3d_base()
    #[2] 3차원 좌표에서 2차원 연결좌표 찾기(1차목적지)
    for r in range(br,br+M):
        for c in range(bc,bc+M):
            if arr[r][c] != 3:
                continue
            if arr[r][c+1] == 0: # 우측에 2차 시작점
                return 0,M-1,(M-1)-(r-br),r,c+1
            elif arr[r][c-1] == 0: # 좌측에 출구
                return 1,M-1,r-br,r,c-1
            elif arr[r+1][c] == 0:  # 아래쪽으로 출구
                return 2,M-1,c-bc,r+1,c
            elif arr[r-1][c] == 0: # 위쪽으로 출구
                return 3,M-1,(M-1)-(c-bc),r-1,c
    return -1

# print(ek_3d, ei_3d, ej_3d, sr,sc)
left_nxt = {0:2, 2:1, 1:3, 3:0}
right_nxt = {0:3, 2:0, 1:2, 3:1}
from collections import deque
def bfs_3d(sk, si, sj,ek, ei, ej):
    q = deque()
    v = [[[0] * M for _ in range(M)] for _ in range(5)]

    q.append((sk,si,sj))
    v[sk][si][sj] = 1

    while q:
        ck,ci,cj = q.popleft()
        # 종료조건, 만약 목적지에 도달한다면 거리를 return
        if (ck,ci,cj) == (ek,ei,ej):
            return v[ck][ci][cj]
        # 4방향, 범위내/범위밖 -> 다른 평면 이동처리
        for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni,nj = ci + di, cj + dj
            # 범위 밖
            if ni < 0: # 위쪽 범우 ㅣ이탈
                if ck == 0: nk,ni,nj = 4,(M-1)-cj,M-1
                elif ck == 1: nk,ni,nj = 4,cj,0
                elif ck == 2: nk,ni,nj = 4,M-1,cj
                elif ck == 3: nk,ni,nj = 4,0,(M-1)-cj
                elif ck == 4: nk,ni,nj = 3,0,(M-1)-cj
            elif ni >= M: # 아래 범위 이탈
                if ck == 4: nk,ni,nj = 2,0,cj
                else: continue
            elif nj < 0: # 왼족 범위 이탈
                if ck == 4: nk,ni,nj = 1,0,ci
                else:
                    nk,ni,nj = left_nxt[ck],ci,M-1
            elif nj >= M: # 오른쪽 범위 이탈
                if ck == 4: nk,ni,nj = 0,0,(M-1)-ci
                else:
                    nk,ni,nj = right_nxt[ck],ci,0
            else:
                nk = ck
            # 미방문, 조건 맞으면
            if v[nk][ni][nj] == 0 and arr3[nk][ni][nj] == 0:
                q.append((nk,ni,nj))
                v[nk][ni][nj] = v[ck][ci][cj] + 1
    # 이곳에 온건? 경로 없음
    return -1

def bfs_2d(v,dist,si,sj,ei,ej):
    q = deque()
    q.append((si,sj))
    v[si][sj] = dist

    while q:
        ci,cj = q.popleft()
        # 4방향, 범위내, 미방문/조건 맞으면(v[ci][cj]+1<v[ni][nj])
        if (ci,cj) == (ei,ej):
            return v[ci][cj]

        for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni,nj = ci +di, cj + dj
            if 0<=ni<N and 0<=nj<N and arr[ni][nj] == 0 and v[ni][nj] > v[ci][cj] + 1:
                q.append((ni,nj))
                v[ni][nj] = v[ci][cj] + 1
    # 목적지를 찾지 못하면
    return -1 
# [1] 주요 위치들 찾기

# 3차원 시작, 3차원 끝, 2차원 시작, 2차원 끝 좌표 탐색
sk_3d, si_3d, sj_3d = find_3d_start()
er,ec = find_2d_end()
ek_3d, ei_3d, ej_3d, sr,sc = find_3d_end_2d_start()

# [2] 3차원 공간 탐색: 시작위치 -> 탈출위치거리 탐색 (BFS 최단거리)
dist = bfs_3d(sk_3d, si_3d, sj_3d,ek_3d, ei_3d, ej_3d)

# E W S N
di = [0,0,1,-1]
dj = [1,-1,0,0]
if dist != -1:
    # [3] 2차원 탐색준비: 시간이상현상 처리해서 v에 시간표시 : BFS 확산시 그보다 작으면 통과하게 표시
    v = [[401] * N for _ in range(N)]
    for wi,wj,wd,wv in wall: # wv 단위로 wd방향으로 확산
        v[wi][wj]=1
        for mul in range(1,N+1):
            wi,wj = wi + di[wd], wj+dj[wd]
            if 0<=wi<N and 0<=wj<N and arr[wi][wj] == 0 and (wi,wj) != (er,ec):
                v[wi][wj]=wv*mul
            else:
                break
    # [4] 2차원 시작위치에서 BFS로 탈출구 탐색 (v에 적혀있는 값보다 작을때 지나감)
    dist = bfs_2d(v,dist,sr,sc,er,ec)
print(dist)