'''
내 풀이는 조합을 통해서 직사각형의 양 끝점을 찾고 거기서 조건문을 돌리는 형태 
'''
# N,M = tuple(map(int,input().split())) 
# board = [list(map(int,input().split())) for _ in range(N)]
# coords = [(i,j) for i in range(N) for j in range(M)]

# def gen_combi(arr,n):
#     res = []
#     if n == 0:
#         return [[]]
#     for i in range(len(arr)):
#         elem = arr[i]
#         for C in gen_combi(arr[i+1:],n-1):
#             res.append([elem]+C)
#     return res
# 
# # print(coords)
# # print(gen_combi(coords,2))
# 
# def check_positive(arr):
#     flag = True
#     r1,c1,r2,c2 = arr[0][0],arr[0][1],arr[1][0],arr[1][1]
#     start_r, start_c = min(r1,r2), min(c1,c2)
#     end_r, end_c = max(r1,r2), max(c1,c2)
# 
#     for r in range(start_r,end_r+1):
#         for c in range(start_c,end_c+1):
#             if board[r][c] <= 0:
#                 flag = False
#     return flag
# 
# def get_size(arr):
#     r1,c1,r2,c2 = arr[0][0],arr[0][1],arr[1][0],arr[1][1]
#     return (abs(r1-r2)+1) * (abs(c1-c2)+1)
# 
# coords_cand = gen_combi(coords,2)
# 
# max_ans = -1
# for i in range(len(coords_cand)):
#     cands = coords_cand[i]
#     if check_positive(cands):
#         max_ans = max(max_ans,get_size(cands))
#     else:
#         max_ans = max_ans
# print(max_ans)
# 
'''
답지 풀이는 그냥 모든 for문 순회시키기?
'''
N,M = tuple(map(int,input().split())) 
board = [list(map(int,input().split())) for _ in range(N)] 

# (r1,c1),(r2,c2)를 꼭지점으로 하는 사각형 내부 값이 전부 양수인지
def postivie_rect(r1,c1,r2,c2): 
    return all([
        board[i][j] > 0 
        for r in range(r1,r2+1)
        for c in range(c1,c2+1)
    ])
ans = -1 
# 직사각형 양끝점을 정해 해당 직사각형 내부가 양수일 때만 갱신 
for i in range(N): 
    for j in range(M): 
        for k in range(i,N): 
            for l in range(j,M): 
                if postivie_rect(i,j,k,l): 
                    ans = max(ans, (k-i+1)*(l-j+1))
print(ans)