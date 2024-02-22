N,M = map(int,input().split()) 
board = list(list(map(int,input().split())) for _ in range(N)) 
# m개만큼 있는지 체크하기 
def check(arr): 
    global M
    flag = True  
    for i in range(len(arr)-M+1): 
        if arr[i:i+M].count(arr[i]) == M: 
            flag = True 
        else: 
            flag = False 
        # for j in range(i+1, len(arr)-M): 
        #     if arr[i] != arr[j]: 
        #         flag = False 
        #         continue 
        #     else: 
        #         flag = True 
    return flag 

def transpose(arr): 
    tmp = [[0] * len(arr[0]) for _ in range(len(arr))] 
    for i in range(len(arr)): 
        for j in range(len(arr[0])):
            tmp[i][j] = arr[j][i] 
    return tmp 
# 가로열 위주로 체크하기 
ans = 0 
for i in range(N): 
    if check(board[i]):        
        ans += 1 
# 세로로 읽는 방안이 생각 안 나서.. 행렬을 전치하고 다시 카운팅
trans_board = transpose(board) 
for i in range(N): 
    if check(trans_board[i]): 
        ans += 1
print(ans) 
'''
1 2 2
1 3 4
1 2 3

가로 
0 0 / 0 1 / 0 2

세로 
0 0 
1 0 
2 0 

0 1 
1 1 
2 1 

0 2 
1 2 
2 2 
'''