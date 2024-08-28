N,M = tuple(map(int,input().split()))
board = [list(map(int,input().split())) for _ in range(N)]

row_list = []
for i in range(N):
    row_list.append(board[i])

for j in range(N):
    mid = [] * N
    for i in range(N):
        mid.append(board[i][j])
    row_list.append(mid)
# 작위적이지만 어찌저찌 구함...
# print(row_list)

# 이제 해피함수 만들기
def check_happy(arr):
    for i in range(N-M+1):
        # print(i)
        if arr[i] == arr[i+M-1]:
            return True
    return False

cnt = 0
for r in row_list:
    if check_happy(r):
        cnt += 1

print(cnt)