from collections import deque 

drs, dcs = [0,0,0,-1,1], [0,1,-1,0,0] 
move = {1:(0,1), 2:(0,-1), 3:(1,-1), 4:(1,1)}

N,M,r,c,K = map(int,input().split()) 
dice = [deque([0,0,0,0]), deque([0,0,0,0])]
board = [list(map(int,input().split())) for _ in range(N)] 
orderlist = list(map(int,input().split())) 

def roll(): 
    global r,c 
    for i in orderlist: 
        nr = r + drs[i] 
        nc = c + dcs[i] 

        if 0 <= nr < N and 0 <= nc < M: 
            dice[move[i][0]].rotate(move[i][1]) 
            dice[1-move[i][0]][1] = dice[move[i][0]][1] 
            dice[1-move[i][0]][3] = dice[move[i][0]][3] 
            if board[nr][nc] == 0: 
                board[nr][nc] = dice[0][3] 
            else: 
                dice[0][3], dice[1][3] = board[nr][nc], board[nr][nc] 
                board[nr][nc] = 0 
            print(dice[0][1]) 
            r,c = nr,nc 
def main(): 
    global N,M,r,c,K,dice,board,orderlist
    roll() 
main()