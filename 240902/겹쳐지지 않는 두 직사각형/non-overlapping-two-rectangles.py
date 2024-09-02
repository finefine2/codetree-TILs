N,M = tuple(map(int,input().split()))
board = [list(map(int,input().split())) for _ in range(N)]
coords = [
    (i,j)
    for i in range(N)
    for j in range(M)
]
def gen_combi(arr,n):
    res = []
    if n == 0:
        return [[]]

    for i in range(len(arr)):
        elem = arr[i]
        for C in gen_combi(arr[i:],n-1):
            res.append([elem]+C)
    return res

coords_cand = gen_combi(coords,2)
# print(coords_cand)
# print(len(coords_cand))

# ex = coords_cand[1]
def calc_rect(arr):
    r1,c1,r2,c2 = arr[0][0],arr[0][1],arr[1][0],arr[1][1]

    start_r, start_c = min(r1,r2),min(c1,c2)
    end_r, end_c = max(r1,r2), max(c1,c2)
    ans = 0
    for r in range(start_r,end_r+1):
        for c in range(start_c,end_c+1):
            ans += board[r][c]
    return ans
# print(calc_rect(ex)
def check_overlap(arr1,arr2):
    flag = True
    r1,c1,r2,c2 = arr1[0][0],arr1[0][1],arr1[1][0],arr1[1][1]
    r3,c3,r4,c4 = arr2[0][0],arr2[0][1],arr2[1][0],arr2[1][1]

    s_r1, s_c1 = min(r1,r2), min(c1,c2)
    e_r1, e_c1 = max(r1,r2), max(c1,c2)

    s_r2, s_c2 = min(r3,r4), min(c3,c4)
    e_r2, e_c2 = max(r3,r4), max(c3,c4)

    return not (e_r1 < s_r2 or s_r1 > e_r2 or s_c1 > e_c2 or e_c1 < s_c2)
# print(check_overlap([(0,0),(0,0)],[(0,0),(1,0)]))
# print(check_overlap([(0,0),(0,0)],[(1,1),(1,0)]))
max_ans = -1000000
for i in range(len(coords_cand)-1):
    for j in range(i+1):
        first = coords_cand[i]
        second = coords_cand[j]

        if not check_overlap(first,second):
            # print(f"first is {first} and second is {second}")
            mid1 = calc_rect(first)
            mid2 = calc_rect(second)
            max_ans = max(max_ans,mid1+mid2)
        else:
            max_ans = max_ans
            continue

print(max_ans)