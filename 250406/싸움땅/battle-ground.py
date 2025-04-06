class GameSimulator:
    def __init__(self, N, M, K):
        self.N = N
        self.M = M
        self.K = K
        self.board = [[0] * N for _ in range(N)]
        self.guns = [[[] for _ in range(N)] for _ in range(N)]
        self.players = {}
        self.drs, self.dcs = [-1,0,1,0], [0,1,0,-1]
        self.opp = {0:2, 1:3, 2:0, 3:1}

    def initialize_board(self):
        # 총 정보 초기화
        initial_board = [list(map(int,input().split())) for _ in range(self.N)]
        for r in range(self.N):
            for c in range(self.N):
                if initial_board[r][c] > 0:
                    self.guns[r][c].append(initial_board[r][c])

    def initialize_players(self):
        # 플레이어 정보 초기화
        for m in range(1, self.M+1):
            r,c,d,p = map(int,input().split())
            self.players[m] = [r-1,c-1,d,p,0,0]  # r,c,dir,power,gun,score
            self.board[r-1][c-1] = m

    def in_range(self, r, c):
        return 0 <= r < self.N and 0 <= c < self.N

    def leave_position(self, num, cr, cc, cd, cp, cg, cs):
        # 패배한 플레이어의 이동
        for k in range(4):
            nr, nc = cr + self.drs[(cd+k)%4], cc + self.dcs[(cd+k)%4]
            if self.in_range(nr,nc) and self.board[nr][nc] == 0:
                if self.guns[nr][nc]:
                    cg = max(self.guns[nr][nc])
                    self.guns[nr][nc].remove(cg)
                self.board[nr][nc] = num
                self.players[num] = [nr,nc,(cd+k)%4,cp,cg,cs]
                return

    def simulate_round(self):
        for i in self.players:
            # 현재 플레이어 정보
            cr,cc,cd,cp,cg,cs = self.players[i]
            
            # 이동
            nr,nc = cr + self.drs[cd], cc + self.dcs[cd]
            if not self.in_range(nr,nc):
                cd = self.opp[cd]
                nr,nc = cr + self.drs[cd], cc + self.dcs[cd]
            self.board[cr][cc] = 0

            # 빈 칸으로 이동
            if self.board[nr][nc] == 0:
                if self.guns[nr][nc]:
                    mx = max(self.guns[nr][nc])
                    if mx > cg:
                        if cg > 0:
                            self.guns[nr][nc].append(cg)
                        self.guns[nr][nc].remove(mx)
                        cg = mx
                self.board[nr][nc] = i
                self.players[i] = [nr,nc,cd,cp,cg,cs]

            # 전투 발생
            else:
                enemy = self.board[nr][nc]
                er,ec,ed,ep,eg,es = self.players[enemy]
                
                # 전투 승패 판정
                if cp + cg > ep + eg or (cp+cg==ep+eg and cp>ep):
                    # 승리
                    cs += (cp+cg) - (ep+eg)
                    self.leave_position(enemy,nr,nc,ed,ep,0,es)
                    
                    if cg < eg:
                        if cg > 0:
                            self.guns[nr][nc].append(cg)
                        cg = eg
                    else:
                        if eg > 0:
                            self.guns[nr][nc].append(eg)
                    self.board[nr][nc] = i
                    self.players[i] = [nr,nc,cd,cp,cg,cs]
                else:
                    # 패배
                    es += (ep+eg) - (cp+cg)
                    self.leave_position(i,nr,nc,cd,cp,0,cs)
                    
                    if eg < cg:
                        if eg > 0:
                            self.guns[nr][nc].append(eg)
                        eg = cg
                    else:
                        if cg > 0:
                            self.guns[nr][nc].append(cg)
                    self.board[nr][nc] = enemy
                    self.players[enemy] = [nr,nc,ed,ep,eg,es]

    def get_scores(self):
        return " ".join(str(self.players[i][5]) for i in range(1, self.M+1))

def main():
    N,M,K = map(int,input().split())
    game = GameSimulator(N, M, K)
    game.initialize_board()
    game.initialize_players()
    
    for _ in range(K):
        game.simulate_round()
    
    print(game.get_scores())

main()