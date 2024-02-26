N, T = map(int,input().split()) 
up_board = list(map(int,input().split())) 
down_board = list(map(int,input().split())) 
'''
1 2 3       1 1 2
6 5 1       3 6 5
'''

dow_tmp = down_board[N-1] 

    
def move(): 
    up_tmp = up_board[N-1]
    dow_tmp = down_board[N-1] 

    for i in range(N-1,0,-1):
        up_board[i] = up_board[i-1] 
    up_board[0] = dow_tmp
    
    for i in range(N-1,0,-1): 
        down_board[i] = down_board[i-1] 
    down_board[0] = up_tmp
for _ in range(T): 
    move() 
for u in up_board:
    print(u,end=" ")
print()
for d in down_board: 
    print(d,end=" ")