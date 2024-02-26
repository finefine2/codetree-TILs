N,M = map(int,input().split()) 

board = [list(map(int,input().split())) for _ in range(N)] 

shapes = [
    [[1, 1, 0],
    [1, 0, 0],
    [0, 0, 0]],

    [[1, 1, 0],
    [0, 1, 0],
    [0, 0, 0]],

    [[1, 0, 0],
    [1, 1, 0],
    [0, 0, 0]],

    [[0, 1, 0],
    [1, 1, 0],
    [0, 0, 0]],

    [[1, 1, 1],
    [0, 0, 0],
    [0, 0, 0]],

    [[1, 0, 0],
    [1, 0, 0],
    [1, 0, 0]],
]

def get_max_sum(r,c): 
    max_sum = 0 
    for i in range(6): 
        is_possible = True 
        sum_of_nums = 0 
        for dr in range(0,3): 
            for dc in range(0,3): 
                if shapes[i][dr][dc] == 0: 
                    continue 
                if r + dr >= N or c + dc >= M: 
                    is_possible = False 
                else: 
                    sum_of_nums += board[r+dr][c+dc] 
        if is_possible: 
            max_sum = max(max_sum, sum_of_nums) 
    return max_sum 
ans = 0 

for i in range(N): 
    for j in range(M): 
        ans = max(ans, get_max_sum(i,j)) 
print(ans)