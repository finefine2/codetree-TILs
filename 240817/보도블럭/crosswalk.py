# 모든 행과 열에 대한 검사가 필요 
# 하나의 행 혹은 열을 고르게 되면, 길이가 n인 수열이 주어질 때 문제 조건을 만족하는 경사로를 놓을 수 있는지 판단

# 필요한 모든 구간에 대해 각 칸마다 경사로가 몇개 놓이나? 

# 지정된 행 또는 열에 위치한 n개 원소들을 1차원 리스트로 
# 길이가 n인 해당 수열이 지나갈 수 있는 곳인지 판단하기 

# 1. 인접한 곳의 높이차가 2 이상인지 확인 
# 존재하면 이는 불가능
# 2. 꼭 놓아야 할 경사로 확인, 경사로가 겹치는지 판단 위해 경사로가 놓일 때마다 각 칸에 1을 더함 
# 2-1 직각삼각형이 필요한 곳을 체크  
# L 만큼의 여유 공간이 있는지 
# [i+1,i+L]구간에 전부 같은 숫자가 놓엿는지
# 3. 꼭 놓아야 했던 경사로끼리 겹쳤는지 

N,L = map(int,input().split()) 
board = [list(map(int,input().split())) for _ in range(N)] 
arr = [0 for _ in range(N)] 

# 각 칸마다 경사로가 몇번씩 놓였는지를 체크 
# 경사로 겹쳤는지 여부 확인용 
ramp_cnt = [0 for _ in range(N)] 

# arr의 [l,r]구간의 원소가 전부 동일한지 확인 
def all_same(l,r): 
    return len(set(arr[l:r+1])) == 1 
# arr가 지나갈 수 있나? 
def can_pass(): 
    global ramp_cnt
    # step1 
    # 인접한 곳의 높이 차가 2이상인지 확인. 존재하면 불가능 
    for i in range(N-1): 
        if abs(arr[i] - arr[i+1]) >= 2: 
            return False
    # 각 위치마다 경사로의 개수를 0으로 초기화 
    ramp_cnt = [0 for _ in range(N)] 

    # step2 
    # 꼭 놓아야 할 경사로를 확인 
    # 직각삼각형이 필요한 곳을 체크 
    for i in range(N-1): 
        # [i+1,i+L]까지 경사로를 놓아야하는 경우 
        if arr[i] == arr[i+1] + 1: 
            if i + L >= N: 
                return False 
            # 경사로가 놓일 높이가 전부 같나? 
            if not all_same(i+1,i+L): 
                return False

            for j in range(i+1,i+L+1): 
                ramp_cnt[j] += 1 
    for i in range(1,N): 
        if arr[i] == arr[i-1] + 1: 
            if i - L < 0: 
                return False 
            if not all_same(i-L, i-1): 
                return False
            for j in range(i-L,i): 
                ramp_cnt[j] += 1 

    if any([cnt >= 2 for cnt in ramp_cnt]): 
        return False
    return True 
ans = 0 

for row in range(N): 
    for col in range(N): 
        arr[col] = board[row][col] 

    if can_pass(): 
        ans += 1 

for col in range(N): 
    for row in range(N): 
        arr[row] = board[row][col] 
    if can_pass(): 
        ans += 1
print(ans)