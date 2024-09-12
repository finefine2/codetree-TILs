import sys
INT_MAX = sys.maxsize
# 0 blank 1 person 2 clinic
N,M = tuple(map(int,input().split()))
board = []
people = []
clinics = []
for i in range(N):
    board.append(list(map(int,input().split())))
    for j in range(N):
        if board[i][j] == 2:
            clinics.append([i,j])
        elif board[i][j] == 1:
            people.append([i,j])

def gen_combi(arr,n):
    res = []
    if n == 0:
        return [[]]
    for i in range(len(arr)):
        elem = arr[i]
        for C in gen_combi(arr[i+1:],n-1):
            res.append([elem]+C)
    return res
# M 개의 병원을 고른다
# len(clinics)-M 개 병원을 0으로 바꿔준다
choose_clinics = gen_combi(clinics,M)
# 고른 병원들에 대해 병원 거리를 측정한다
ans = INT_MAX

for i in range(len(choose_clinics)):
    # 새로 루프가 돌 때마다 보드 초기화는 해야함
    mid = 0
    go_clinic = choose_clinics[i]
    # 병원 거리를 측정하는 법
    # 사람별로 병원 거리를 측정하되, 가장 가까운 걸 남긴다
    for pr,pc in people:
        dist = INT_MAX
        for cr,cc in go_clinic:
            dist = min(dist,abs(pr-cr)+abs(pc-cc))
        mid += dist
    ans = min(ans,mid)
print(ans)