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
# m개 이상 연속으로 같은 수열인지
def check_happy(arr):
    consec_cnt, max_cnt = 1,1
    for i in range(1,N):
        if arr[i-1] == arr[i]:
            consec_cnt += 1
        else:
            consec_cnt = 1
        max_cnt = max(max_cnt,consec_cnt)
    return consec_cnt >= M

cnt = 0
for r in row_list:
    if check_happy(r):
        cnt += 1
print(cnt)