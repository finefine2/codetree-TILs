# 유물 조각을 최대한 많이 맞춰 점수를 최대화
# 유물 획득을 위해 가능한 모든 회전을 고려하고, 그 중 최대 점수를 제공하는 회전을 선택
# 격자를 회전시켜 유물을 얻는 과정에서 발생하는 모든 경우를 고려하고, 각 경우의 점수를 계산하여 가장 높은 점수를 얻는 선택

'''
최대 K번의 회전을 통해 유물을 획득
각 회전 후에는 유물 조각을 채우고 다시 유물을 획득하는 과정을 반복하여 추가 점수 획득

알고리즘
- 모든 가능한 회전 (시계방향으로 1,2,3) 과 해당 회전이 적용될 수 있는 격자의 각 시작점을 고려
- 각 회전과 시작점 조합에 대해 회전을 적용한 후 유물 획득 점수를 계산
- BFS 로 같은 숫자가 3개 이상 인접하면 유물로 간주하고 점수 획득
- 가능한 회전 중 최대 점수를 제공하는 경우를 선택. 선택 기준은 가장 높은 점수를 제공하는 회전이고,
- 동일한 점수일 경우 더 적은 회전, 그리고 회전의 중심점이 좌측 상단에 가까울수록 (r,c 가 작을수록)
- 선택된 회전을 적용 후에는 빈 칸을 새로운 유물로 채우고, 다시 유물 점수를 계산하여 추가로 획득하는 점수가 없을 때까지 과정을 반복
- 이를 K번 반복하되, 어떤 회전도 유물 획득에 기여하지 ㅁ소하면 탐사 끝

'''

from collections import deque
K,M  = tuple(map(int,input().split()))

board = [list(map(int,input().split())) for _ in range(5)]
treasures = list(map(int,input().split()))

ans = []

def rotate(sr,sc,arr):
    narr = [x[:] for x in arr]
    for r in range(3):
        for c in range(3):
            narr[sr+r][sc+c] = arr[sr+3-c-1][sc+r]
    return narr

def in_range(r,c):
    return 0 <= r < 5 and 0 <= c < 5

def bfs(v,arr,r,c,clr):
    q = deque()
    q.append((r,c))
    v[r][c] = 1
    drs,dcs = [-1,1,0,0],[0,0,-1,1]

    cnt = 0
    sset = set()
    sset.add((r,c))
    cnt += 1
    while q:
        cr,cc = q.popleft()

        for dr,dc in zip(drs,dcs):
            nr,nc = cr + dr, cc + dc
            if in_range(nr,nc) and v[nr][nc] == 0 and arr[nr][nc] == arr[cr][cc]:
                q.append((nr,nc))
                v[nr][nc] = 1
                sset.add((nr,nc))
                cnt += 1

    if cnt >= 3:
        if clr == 1:
            for tr,tc in sset:
                arr[tr][tc] = 0
        return cnt
    else:
        return 0

def count_clear(arr,clr):
    v = [[0] * 5 for _ in range(5)]
    cnt = 0
    for r in range(len(arr)):
        for c in range(len(arr[0])):
            if v[r][c] == 0:
                t = bfs(v,arr,r,c,clr)
                cnt += t
    return cnt
for _ in range(K):
    max_cnt = 0

    for rot in range(1,4):
        for sr in range(3):
            for sc in range(3):
                nboard = [x[:] for x in board]
                for _ in range(rot):
                    nboard = rotate(sr,sc,nboard)
                cnt = count_clear(nboard,0)
                if max_cnt < cnt:
                    max_cnt = cnt
                    mboard = nboard

    if max_cnt == 0:
        break

    # 보드 선택 후 없애기
    board = mboard
    cnt = 0
    while True:
        t = count_clear(board,1)
        if t == 0:
            break # 연쇄획득 종료 -> 다음 턴
        cnt += t

        # 연쇄 획득
        for c in range(5):
            for r in range(4,-1,-1):
                if board[r][c] == 0:
                    board[r][c] = treasures.pop(0)
    ans.append(cnt)
for a in ans:
    print(a,end=" ")