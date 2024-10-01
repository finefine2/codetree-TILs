from collections import deque 

N,M = tuple(map(int,input().split())) 
RED = 0 
ROCK = -1 
EMPTY = M+1 
EMPTY_BUNDLE = (-1,-1,-1,-1) 
board = [list(map(int,input().split())) for _ in range(N)] 

q = deque() 
visited = [[0] * N for _ in range(N)] 
ans = 0 

def in_range(r,c): from collections import deque

RED = 0
ROCK = -1
EMPTY = -2
EMPTY_BUNDLE = (-1, -1, -1, -1)

# 변수 선언 및 입력:
n, m = tuple(map(int, input().split()))
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
temp = [
    [EMPTY for _ in range(n)]
    for _ in range(n)
]

bfs_q = deque()
visited = [
    [False for _ in range(n)]
    for _ in range(n)
]

ans = 0


def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n


# 같은 색이거나, 빨간색 폭탄인 경우에만 이동이 가능합니다.
def can_go(x, y, color):
    return in_range(x, y) and not visited[x][y] and (
        grid[x][y] == color or grid[x][y] == RED
    )


def bfs(x, y, color):
    # visited 값을 초기화합니다.
    for i in range(n):
        for j in range(n):
            visited[i][j] = False

    # 시작점을 표시합니다.
    visited[x][y] = True
    bfs_q.append((x, y))

    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

    # BFS 탐색을 수행합니다.
    while bfs_q:
        curr_x, curr_y = bfs_q.popleft()

        for dx, dy in zip(dxs, dys):
            new_x, new_y = curr_x + dx, curr_y + dy

            if can_go(new_x, new_y, color):
                bfs_q.append((new_x, new_y))
                visited[new_x][new_y] = True
                

# (x, y) 지점을 시작으로 bundle 정보를 계산해 반환합니다.
def get_bundle(x, y):
    # Step1. (x, y)를 시작으로 bfs 탐색을 진행합니다.
    bfs(x, y, grid[x][y]);

    # Step2. bundle 정보를 계산해 반환합니다.
    bomb_cnt, red_cnt = 0, 0
    standard = (-1, -1)

    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                continue

            bomb_cnt += 1
            
            if grid[i][j] == RED:
                red_cnt += 1
            elif (i, -j) > standard:
                standard = (i, -j)
    
    std_x, std_y = standard;
    return (bomb_cnt, -red_cnt, std_x, std_y)


# 우선순위에 따라 쉽게 계산하기 위해
# (폭탄 묶음의 크기, -빨간색 폭탄의 수, 행 번호, -열 번호)
# 순서대로 값을 넣어줍니다.
def find_best_bundle():
    best_bundle = EMPTY_BUNDLE

    # 빨간색이 아닌 폭탄들에 대해서만 전부 탐색합니다.
    for i in range(n):
        for j in range(n):
            if grid[i][j] >= 1:
                bundle = get_bundle(i, j)
                if bundle > best_bundle:
                    best_bundle = bundle
    
    return best_bundle


def remove():
    for i in range(n):
        for j in range(n):
            if visited[i][j]:
                grid[i][j] = EMPTY


def gravity():
    # Step1.
    # 중력 작용을 쉽게 구현하기 위해
    # temp 배열을 활용합니다.
    for i in range(n):
        for j in range(n):
            temp[i][j] = EMPTY
    
    # Step2.
    for j in range(n):
        # 아래에서 위로 올라오면서
        # 해당 위치에 폭탄이 있는 경우에만 temp에 
        # 쌓아주는 식으로 코드를 작성할 수 있습니다.

        # 단, 돌이 있는 경우에는
        # 위에부터 쌓일 수 있도록 합니다.
        last_idx = n - 1
        for i in range(n - 1, -1, -1):
            if grid[i][j] == EMPTY:
                continue
            if grid[i][j] == ROCK:
                last_idx = i
            temp[last_idx][j] = grid[i][j]
            last_idx -= 1
            
    # Step3. 다시 temp 배열을 옮겨줍니다.
    for i in range(n):
        for j in range(n):
            grid[i][j] = temp[i][j]


# 반시계 방향으로 90' 만큼 회전합니다.
def rotate():
    # Step1. 
    # 회전 과정을 쉽게 구현하기 위해
    # temp 배열을 활용합니다.
    for i in range(n):
        for j in range(n):
            temp[i][j] = EMPTY

    # Step2.
    # 기존 격자를 반시계 방향으로 90도 회전했을 때의 결과를
    # temp에 저장해줍니다.
    for j in range(n - 1, -1, -1):
        for i in range(n):
            temp[n - 1 - j][i] = grid[i][j]

    # Step3.
    # 다시 temp 배열을 옮겨줍니다.
    for i in range(n):
        for j in range(n):
            grid[i][j] = temp[i][j]


def clean(x, y):
    # Step1. (x, y)를 시작으로 지워야할 폭탄 묶음을 표시합니다.
    bfs(x, y, grid[x][y])

    # Step2. 폭탄들을 전부 지워줍니다.
    remove()

    # Step3. 중력이 작용합니다.
    gravity()


def simulate():
    global ans
    
    # Step1. 크기가 최대인 폭탄 묶음을 찾습니다.
    best_bundle = find_best_bundle()
    bomb_cnt, _, x, y = best_bundle

    # 만약 폭탄 묶음이 없다면, 종료합니다.
    if best_bundle == EMPTY_BUNDLE or bomb_cnt <= 1:
        return False

    # Step2. 선택된 폭탄 묶음에 해당하는 폭탄들을 전부 제거 후
    #        중력이 작용합니다.
    ans += bomb_cnt * bomb_cnt
    clean(x, -y)

    # Step3. 반시계 방향으로 90' 만큼 회전합니다.
    rotate()

    # Step4. 중력이 작용합니다.
    gravity()

    return True


# 끝나기 전까지 시뮬레이션을 반복합니다.
while True:
    keep_going = simulate()
    
    if not keep_going:
        break

print(ans)
    return 0<=r<N and 0<=c<N 

def can_go(r,c,color): 
    return in_range(r,c) and not visited[r][c] and (board[r][c] == color or board[r][c] == RED) 

def bfs(sr,sc,color): 
    # initialize visited 
    for r in range(N): 
        for c in range(N): 
            visited[r][c] = 0 
    visited[sr][sc] = 1 
    q.append((sr,sc)) 

    drs,dcs = [0,1,0,-1],[1,0,-1,0] 
    while q: 
        cr,cc = q.popleft() 
        for dr,dc in zip(drs,dcs): 
            nr,nc = cr + dr, cc + dc 
            if can_go(nr,nc,color): 
                q.append((nr,nc)) 
                visited[nr][nc] = 1 
def get_bundle(sr,sc): 
    bfs(sr,sc,board[sr][sc]) 

    bomb_cnt,red_cnt = 0,0 
    standard = (-1,-1) 
    for r in range(N): 
        for c in range(N): 
            if not visited[r][c]: 
                continue 
            bomb_cnt += 1 
            if board[r][c] == RED: 
                red_cnt += 1 
            elif (r,-c) > standard: 
                standard = (r,-c) 
    std_r,std_c = standard
    return (bomb_cnt,-red_cnt,std_r,std_c) 

def find_best_bundle(): 
    best_bundle = EMPTY_BUNDLE
    for r in range(N): 
        for c in range(N): 
            if board[r][c] >= 1: 
                bundle = get_bundle(r,c) 
                if bundle > best_bundle: 
                    best_bundle = bundle
    return best_bundle

def remove(): 
    for r in range(N): 
        for c in range(N): 
            if visited[r][c]: 
                board[r][c] = EMPTY 

def gravity(): 
    for sr in range(0,N-1): 
        for sc in range(N): 
            cr,cc = sr,sc 
            while in_range(cr,cc) and 0<=board[cr][cc]<=M and board[cr+1][cc] == EMPTY: 
                board[cr][cc],board[cr+1][cc] = board[cr+1][cc], board[cr][cc] 
                cr -= 1

def clean(r,c): 
    bfs(r,c,board[r][c]) 
    remove() 
    gravity()
ans = 0 
while True: 
    best_bundle = find_best_bundle() 
    bomb_cnt,_,r,c = best_bundle
    if best_bundle == EMPTY_BUNDLE or bomb_cnt <= 1: 
        break 
    ans += bomb_cnt ** 2 
    clean(r,-c) 
    board = list(map(list,zip(*board)))[::-1] 
    gravity() 
print(ans)