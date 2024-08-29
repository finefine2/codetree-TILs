N,M = tuple(map(int,input().split()))
board = [list(map(int,input().split())) for _ in range(N)]
# 생각이 안나므로 1번 블럭 2번 블럭 3번 블럭 4번 블럭 5번 블럭 6번 블럭 각각에 대해 전부 계산하는 수 밖에

def calc_1():
    max_cnt = -1
    for i in range(N-1):
        for j in range(M-1):
            cnt = board[i][j] + board[i][j+1] + board[i+1][j]
            # print(f"current positions are {i},{j}")
            max_cnt = max(cnt,max_cnt)
    return max_cnt
def calc_2():
    max_cnt = -1
    for i in range(N-1):
        for j in range(M-1):
            cnt = board[i][j] + board[i][j+1] + board[i+1][j+1]
            max_cnt = max(cnt,max_cnt)
    return max_cnt
def calc_3():
    max_cnt = -1
    for i in range(N-1):
        for j in range(M-1):
            cnt = board[i][j+1] + board[i+1][j] + board[i+1][j+1]
            max_cnt = max(cnt,max_cnt)
    return max_cnt
def calc_4():
    max_cnt = -1
    for i in range(N-1):
        for j in range(M-1):
            cnt = board[i][j] + board[i+1][j] + board[i+1][j+1]
            max_cnt = max(cnt,max_cnt)
    return max_cnt

def calc_5():
    max_cnt = -1
    for i in range(N):
        cnt = 0
        for j in range(M-2):
            for k in range(3):
                cnt += board[i][j+k]
                # print(f"current positions are {i},{j+k}")
            max_cnt = max(max_cnt,cnt)
    return max_cnt
def calc_6():
    max_cnt = -1
    for j in range(M):
        cnt = 0
        for i in range(N-2):
            for k in range(3):
                cnt += board[i+k][j]
                # print(f"current postitions are {i+k},{j}")
            max_cnt = max(max_cnt,cnt)
    return max_cnt

# 2x2 board로 생각하고 구현
# print(calc_1())
# print(calc_2())
# 길이 3짜리 막대들은 해결
# print(calc_5())
# print(calc_6())
print(max(calc_1(),calc_2(),calc_3(),calc_4(),calc_5(),calc_6()))