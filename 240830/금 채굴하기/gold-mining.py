N,M = tuple(map(int,input().split()))

board = [list(map(int,input().split())) for _ in range(N)]
K = 0
max_gold = 0

def gold_expense(k): 
    return k*k + (k+1) * (k+1) 

def get_gold(r,c,k): 
    return sum([
        board[i][j] 
        for i in range(N)
        for j in range(N)
        if abs(r-i) + abs(c-j) <= k 
    ])

for r in range(N):
    for c in range(N):
        for K in range(2*N-1):
            num = get_gold(r,c,K) 
            if num * M >= gold_expense(K): 
                max_gold = max(max_gold,num) 
 
print(max_gold)