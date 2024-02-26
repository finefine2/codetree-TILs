N = int(input()) 
board = [list(map(int,input().split())) for _ in range(N)] 


'''
1번 선분과 3번 선분의 길이만 변화를 준다고 생각해도 괜찮을지도 

'''
def in_range(r,c): 
    return 0 <= r < N and 0 <= c < N 

def get_score(r,c,k,l): 
    drs, dcs = [-1,-1,1,1], [1,-1,-1,1]
    move_nums = [k,l,k,l] 

    sum_of_nums = 0 

    for dr, dc, move_num in zip(drs, dcs, move_nums): 
        r,c = r + dr, c + dc 
        if not in_range(r,c): 
            return 0 
        
        sum_of_nums += board[r][c] 
    return sum_of_nums

for i in range(N): 
    for j in range(N): 
        for k in range(1,N): 
            for l in range(1,N): 
                ans = max(ans,get_score(i,j,k,l)) 
print(ans)