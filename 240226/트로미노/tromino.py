N,M = map(int,input().split()) 

board = list(list(map(int,input().split())) for _ in range(N))

# 가능한 블럭들을 나열하기 
blocks = [
    [[1,0],[1,1]],
    [[0,1],[1,1]],
    [[1,1],[0,1]],
    [[1,1],[1,0]],
    [[1,1,1]],
    [[1],[1],[1]]
]

'''
1. 블럭을 하나 고르기 
2. 고른 블럭을 board에 얹고 계산해보기 
- 블럭의 좌표 그리고 board의 좌표는 따로 고려해야하나! 

'''
ans = 0 


# 2 x 2 blocks 
def count1(r,c): 
    ans = board[r][c] + board[r+1][c] + board[r+1][c+1] 
    return ans 
def count2(r,c): 
    ans = board[r][c] + board[r+1][c] + board[r][c+1] 
    return ans 
def count3(r,c): 
    ans = board[r][c] + board[r][c+1] + board[r+1][c+1] 
    return ans 
def count4(r,c): 
    ans = board[r][c+1] + board[r+1][c] + board[r+1][c+1]  
    return ans 
# 1 x 3 
def count5(r,c): 
    ans = board[r][c] + board[r][c+1] + board[r][c+2] 
    return ans 
# 3 x 1 
def count6(r,c): 
    ans = board[r][c] + board[r+1][c] + board[r+2][c] 
    return ans 

for i in range(N-1): 
    for j in range(N-1): 
        ans = max(count1(i,j),ans) 
for i in range(N-1): 
    for j in range(N-1): 
        ans = max(count2(i,j),ans) 
for i in range(N-1): 
    for j in range(N-1): 
        ans = max(count3(i,j),ans) 
for i in range(N-1): 
    for j in range(N-1): 
        ans = max(count4(i,j),ans) 
for i in range(N-3): 
    for j in range(N): 
        ans = max(count6(i,j),ans) 
for i in range(N): 
    for j in range(N-3): 
        ans = max(conut5(i,j),ans) 
print(ans) 
# for b in blocks: 
#     row_end = len(b) 
#     col_end = len(b[0]) 
#     cnt = 0
#     for i in range(len(board)): 
#         for j in range(len(board[0])): 
#             for r in range(row_end): 
#                 for c in range(col_end): 
#                     if i + r >= len(board) or j + c >= len(board[0]): 
#                         continue 
#                     else: 
#                         cnt += board[i][j] * b[r][c]
#                     ans = max(cnt,ans)
# print(ans)