'''
내 풀이는 조합을 써서
직사각형의 양 끝점 두개를 구해놓는 방식
'''
# N,M = tuple(map(int,input().split()))
# board = [list(map(int,input().split())) for _ in range(N)]
# coords = [
#     (i,j)
#     for i in range(N)
#     for j in range(M)
# ]
# def gen_combi(arr,n):
#     res = []
#     if n == 0:
#         return [[]]
#
#     for i in range(len(arr)):
#         elem = arr[i]
#         for C in gen_combi(arr[i:],n-1):
#             res.append([elem]+C)
#     return res
#
# coords_cand = gen_combi(coords,2)
# # print(coords_cand)
# # print(len(coords_cand))
#
# # ex = coords_cand[1]
# def calc_rect(arr):
#     r1,c1,r2,c2 = arr[0][0],arr[0][1],arr[1][0],arr[1][1]
#
#     start_r, start_c = min(r1,r2),min(c1,c2)
#     end_r, end_c = max(r1,r2), max(c1,c2)
#     ans = 0
#     for r in range(start_r,end_r+1):
#         for c in range(start_c,end_c+1):
#             ans += board[r][c]
#     return ans
# # print(calc_rect(ex)
# def check_overlap(arr1,arr2):
#     flag = True
#     r1,c1,r2,c2 = arr1[0][0],arr1[0][1],arr1[1][0],arr1[1][1]
#     r3,c3,r4,c4 = arr2[0][0],arr2[0][1],arr2[1][0],arr2[1][1]
#
#     s_r1, s_c1 = min(r1,r2), min(c1,c2)
#     e_r1, e_c1 = max(r1,r2), max(c1,c2)
#
#     s_r2, s_c2 = min(r3,r4), min(c3,c4)
#     e_r2, e_c2 = max(r3,r4), max(c3,c4)
#
#     return not (e_r1 < s_r2 or s_r1 > e_r2 or s_c1 > e_c2 or e_c1 < s_c2)
# # print(check_overlap([(0,0),(0,0)],[(0,0),(1,0)]))
# # print(check_overlap([(0,0),(0,0)],[(1,1),(1,0)]))
# max_ans = -1000000
# for i in range(len(coords_cand)-1):
#     for j in range(i+1):
#         first = coords_cand[i]
#         second = coords_cand[j]
#
#         if not check_overlap(first,second):
#             # print(f"first is {first} and second is {second}")
#             mid1 = calc_rect(first)
#             mid2 = calc_rect(second)
#             max_ans = max(max_ans,mid1+mid2)
#         else:
#             max_ans = max_ans
#             continue
#
# print(max_ans)
'''
답지의 풀이 
두 직사각형을 전부 잡아서 겹치지 않는 경우 중 최대 값을 구함 
두 직사각형이 겹쳐지는 여부를 확인하기 위해 새로운 arr 활용
'''
import sys
INT_MIN = -sys.maxsize

N,M = tuple(map(int,input().split()))
board = [list(map(int,input().split())) for _ in range(N)]
arr = [[0] * M for _ in range(N)]

def clear_board():
    for i in range(N):
        for j in range(M):
            arr[i][j] = 0

def draw(r1,c1,r2,c2):
    for r in range(r1,r2+1):
        for c in range(c1,c2+1):
            arr[r][c] += 1

def check_board():
    # 동일한 좌표가 2개 직사각형에 모두 포함시 겹친다
    for i in range(N):
        for j in range(M):
            if arr[i][j] >= 2:
                return True
    return False

# (r1,c1),(r2,c2)
# (r3,c3),(r4,c4) 로 이뤄진 두 직사각형이 겹치는지 확인
def overlap(r1,c1,r2,c2,r3,c3,r4,c4):
    clear_board()
    draw(r1,c1,r2,c2)
    draw(r3,c3,r4,c4)
    return check_board()

def rect_sum(r1,c1,r2,c2):
    return sum([
        board[r][c]
        for r in range(r1,r2+1)
        for c in range(c1,c2+1)
    ])

# 첫 직사각형을 잡았을 때 두번째 직사각형이 안 겹치게 잡는 함수
def find_max_sum_with_rect(r1,c1,r2,c2):
    max_sum = INT_MIN
    # (i,j),(k,l) 을 양끝점으로 하는 두번째 사각형을 정해
    # 겹치지 않을 때 중 최대값을 리턴
    for i in range(N):
        for j in range(M):
            for k in range(i,N):
                for l in range(j,M):
                    if not overlap(r1,c1,r2,c2,i,j,k,l):
                        max_sum = max(max_sum,rect_sum(r1,c1,r2,c2)+rect_sum(i,j,k,l))
    return max_sum

# 두 사각형을 잘 잡았을 때의 최대 sum 
def find_max_sum(): 
    max_sum = INT_MIN
    for i in range(N): 
        for j in range(M): 
            for k in range(i,N): 
                for l in range(j,M): 
                    max_sum = max(max_sum,find_max_sum_with_rect(i,j,k,l))
    return max_sum
ans = find_max_sum()
print(ans)