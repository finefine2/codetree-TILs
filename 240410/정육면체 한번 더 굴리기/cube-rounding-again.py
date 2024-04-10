from collections import deque 
def getInput(): 
    N,M = map(int,input().split())
    board = [list(map(int,input().split())) for _ in range(N)] 
    return N, M, board

def move(n, board, dir, x,y, row, column): 
    direction = [(0,1),(1,0),(0,-1),(-1,0)] 
    nx,ny = x + direction[dir][0], y + direction[dir][1] 
    if 0 > nx or n == nx or 0 > ny or n == ny: 
        dir = (dir+2) % 4 
        nx,ny = x + direction[dir][0], y + direction[dir][1] 

    if dir == 0: 
        row.rotate(1) 
        column[0] = row[0] 
        column[2] = row[2]
    elif dir == 1: 
        column.rotate(-1)
        row[0] = column[0] 
        row[2] = column[2] 
    elif dir == 2: 
        row.rotate(-1) 
        column[0] = row[0] 
        column[2] = row[2] 
    elif dir == 3: 
        column.rotate(1) 
        row[0] = column[0] 
        row[2] = column[2] 
    if row[2] > board[nx][ny]: 
        dir = (dir+1) % 4 
    elif row[2] < board[nx][ny]: 
        dir = (dir+3) % 4 
    
    return dir, nx, ny, row, column

def score(n, board, dir, x,y): 
    direction = [(0,1),(1,0),(0,-1),(-1,0)] 
    start = board[x][y] 
    q = deque([(x,y)]) 
    llist = {(x,y)} 
    count = 1 

    while q: 
        x,y = q.popleft() 
        for i in range(4): 
            nx,ny = x + direction[i][0], y + direction[i][1] 
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == start and (nx,ny) not in llist: 
                count += 1 
                q.append((nx,ny)) 
                llist.add((nx,ny)) 
    return start * count 

def main(): 
    N,M, board = getInput() 
    x,y = 0,0 
    dir = 0 
    row = deque([1,3,6,4]) 
    column = deque([1,5,6,2]) 
    ans = 0 

    for _ in range(M): 
        dir, x,y, row, column = move(N, board, dir, x,y, row, column)
        ans += score(N, board, dir, x,y) 
    print(ans) 
main()