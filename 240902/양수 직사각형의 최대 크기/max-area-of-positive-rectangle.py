N,M = tuple(map(int,input().split()))

board = [list(map(int,input().split())) for _ in range(N)]
coords = [(i,j) for i in range(N) for j in range(M)]


def gen_combi(arr,n):
    res = []
    if n == 0:
        return [[]]
    for i in range(len(arr)):
        elem = arr[i]
        for C in gen_combi(arr[i+1:],n-1):
            res.append([elem]+C)
    return res

# print(coords)
# print(gen_combi(coords,2))

def check_positive(arr):
    flag = True
    r1,c1,r2,c2 = arr[0][0],arr[0][1],arr[1][0],arr[1][1]
    start_r, start_c = min(r1,r2), min(c1,c2)
    end_r, end_c = max(r1,r2), max(c1,c2)

    for r in range(start_r,end_r+1):
        for c in range(start_c,end_c+1):
            if board[r][c] <= 0:
                flag = False
    return flag

def get_size(arr):
    r1,c1,r2,c2 = arr[0][0],arr[0][1],arr[1][0],arr[1][1]
    return (abs(r1-r2)+1) * (abs(c1-c2)+1)

coords_cand = gen_combi(coords,2)

max_ans = -1
for i in range(len(coords_cand)):
    cands = coords_cand[i]
    if check_positive(cands):
        max_ans = max(max_ans,get_size(cands))
    else:
        max_ans = max_ans
print(max_ans)