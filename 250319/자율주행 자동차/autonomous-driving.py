drs,dcs = [-1,0,1,0],[0,1,0,-1]

def solve(cr,cc,cd):
    cnt = 0
    while True:
        # 1. 현재 위치 청소
        board[cr][cc] = 2
        cnt += 1

        # 2. 왼쪽 방향으로 순서대로 탐색해서 미청소 영역이 있으면 이동/방향 설정, 없으면 후진
        flag = True
        while flag == True:
            # 왼쪽부터 4방향중 미청소 영역이 있는 경우
            for nd in ((cd+3)%4,(cd+2)%4,(cd+1)%4,cd):
                nr,nc = cr + drs[nd], cc + dcs[nd]
                if board[nr][nc] == 0: # 미청소 영역
                    cr,cc,cd = nr,nc,nd
                    flag = False
                    break
            else: # 4방향 모두 미청소 영역이 없으면 후진
                br,bc = cr - drs[cd], cc- dcs[cd]
                if board[br][bc] == 1: # 벽이면 종료
                    return cnt
                else:
                    cr,cc = br,bc
    return -1

N,M = map(int,input().split())
sr,sc,sd = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]

ans = solve(sr,sc,sd)
print(ans)