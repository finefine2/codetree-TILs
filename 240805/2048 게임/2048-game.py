# 블록 이동과 합치기를 반복 
# 가능한 모든 조합을 시도하기 
# 블록 이동과 합치기는 랜덤하게 발생하지 않으므로 모든 가능성을 체계적으로 발생 

# 격자판을 기울일 때는 먼저 rotate 하고, 블록들을 아래로 '떨구는'연산 수행하기 
# 블록이 만나면 합쳐지는데 한번 합쳐지면 더 이상 합쳐지지 않음 
# 모든 이동이 끝나면 격자판을 원래 상태로 회전시켜 원위치 

# 기울이고 떨구는 연산을 바탕으로 모든 방향에 대해 5번 이동을 시뮬레이션하는 과정을 백트래킹으로 구현 
# 재귀적으로 호출하는 과정에서는 현재까지 이동 방향이 저장된 배열을 사용 
# 이 배열은 각 단계 이동방향을 기록하고, 배열이 완성되면 시뮬레이션 수행 
# 시뮬레이션 후에는 원래 판 상태로 돌아가 다음 이동을 탐색할 수 있도록 격자판을 되도린다 

NUM_MOVES = 5 
NONE = -1 

N = int(input()) 
board = [
    list(map(int,input().split())) for _ in range(N)
]

next_board = [
    [0 for _ in range(N)] for _ in range(N)
]

temp = [
    [0 for _ in range(N)] for _ in range(N)
]

move_dirs = [0 for _ in range(NUM_MOVES)]
ans = 0 

def get_max_block_num(): 
    return max([
        board[i][j]
        for i in range(N) 
        for j in range(N) 
    ])
# 어찌됐든 크게 회전 + 떨구기의 역할
def rotate(): 
    for i in range(N): 
        for j in range(N): 
            next_board[i][j] = 0 

    for i in range(N): 
        for j in range(N): 
            next_board[i][j] = board[N-j-1][i] 
    for i in range(N): 
        for j in range(N): 
            board[i][j] = next_board[i][j] 

def drop(): 
    # next board 초기화 
    for i in range(N): 
        for j in range(N): 
            next_board[i][j] = 0 

    for j in range(N): 
        # 같은 숫자끼리 단 한번 합치기 위해 떨구기 전 숫자 하나를 킵 
        keep_num, next_row = NONE, N-1 
        for i in range(N-1,-1,-1): 
            if not board[i][j]: 
                continue
            if keep_num == NONE: 
                keep_num = board[i][j] 
            # 최근에 관찰한 숫자가 현재 숫자랑 일치하면 하나로 합쳐주고, keep 값을 비움
            elif keep_num == board[i][j]: 
                next_board[next_row][j] = keep_num * 2
                keep_num = NONE 
                next_row -= 1  
            # 가장 최근에 본 숫자와 현재 숫자가 다르면 
            # 최근에 관찰한 숫자를 떨궈주고, keep 값을 갱신 
            else: 
                next_board[next_row][j] = keep_num
                keep_num = board[i][j]  

                next_row -= 1 
        if keep_num != NONE: 
            next_board[next_row][j] = keep_num
            next_row -= 1 
    for i in range(N): 
        for j in range(N): 
            board[i][j] = next_board[i][j] 

# move_dir 방향으로 기울이기 
# 회전을 규칙적으로 하기 위해 
# D R U L 순으로 dr,dc 
def tilt(move_dir): 
    # move_dir 횟수만큼 시계방향으로 90도 회전 반복하여 항상 아래로만 떨구는 것을 진행
    for _ in range(move_dir): 
        rotate() 
    # step2 
    drop() 
    # step3 
    # 4-move_dir 만큼 90도 회전 반복하여 원 상태로 복귀 
    for _ in range(4-move_dir): 
        rotate() 


def simulate(): 
    global ans 
    for i in range(N): 
        for j in range(N): 
            temp[i][j] = board[i][j] 
    # 각 방향으로 기울이기 
    for move_dir in move_dirs: 
        tilt(move_dir)
    ans = max(ans, get_max_block_num()) 
    # 시뮬레이션 전으로 board 되돌리기 
    for i in range(N): 
        for j in range(N): 
            board[i][j] = temp[i][j] 
def search_max_num(cnt): 
    # 5번 방향을 정했으면 직접 시뮬 진행 
    if cnt == NUM_MOVES: 
        simulate() 
        return 
    # 4 방향 중 이동방향 선택 
    for i in range(4): 
        move_dirs[cnt] = i 
        search_max_num(cnt+1) 
search_max_num(0) 
print(ans)