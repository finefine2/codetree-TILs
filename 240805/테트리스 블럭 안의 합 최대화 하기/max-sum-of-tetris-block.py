# 다음 후보의 좌표를, 현재 블록들이 들어있는 리스트를 통해 반복하면서 모든 위치를 탐방하기 
# 그렇게 하면 가운데에서도 양쪽 블럭이 후보에 들어갈 수 있음 

# 후보 좌표를 넣고 재귀를 돌리고 다시 뺴는 식 
# 블럭이 4개일 때 테트로미노가 완성되므로 4번째 depth에서 가지치기를 하면 풀 수 이슴

drs,dcs = [-1,1,0,0], [0,0,-1,1] 
N,M = map(int,input().split()) 
board = [list(map(int,input().split())) for _ in range(N)] 

maxx = -10 
def dfs(level, llist, cnt): 
    global maxx 
    if level == 4: 
        if cnt > maxx: 
            maxx = cnt 
        return 

    for r,c in llist: 
        for i in range(4): 
            nr,nc = r + drs[i], c + dcs[i] 

            if 0<=nr<N and 0<=nc<M and not (nr,nc) in llist: 
                llist.append((nr,nc)) 
                dfs(level+1,llist,cnt+board[nr][nc]) 
                llist.pop() 
for i in range(N): 
    for j in range(M): 
        dfs(1,[(i,j)],board[i][j])
print(maxx)