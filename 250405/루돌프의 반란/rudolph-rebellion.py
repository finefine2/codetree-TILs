from collections import deque

def init_game():
    N, M, P, C, D = map(int, input().split())
    board = [[0] * N for _ in range(N)]
    
    # 루돌프 위치
    rr, rc = map(lambda x: int(x)-1, input().split())
    board[rr][rc] = -1
    
    # 산타 정보 초기화
    santas = {}  # Dictionary로 변경하여 빠른 접근
    scores = [0] * (P+1)
    alive = [True] * (P+1)
    wakeup_turn = [1] * (P+1)
    
    # 산타 입력
    for _ in range(P):
        n, r, c = map(int, input().split())
        santas[n] = [r-1, c-1]
        board[r-1][c-1] = n
        
    return N, M, P, C, D, board, santas, scores, alive, wakeup_turn, rr, rc

def get_closest_santa(rr, rc, santas, alive, N):
    min_dist = float('inf')
    target = None
    
    for idx, pos in santas.items():
        if not alive[idx]:
            continue
        sr, sc = pos
        dist = (rr-sr)**2 + (rc-sc)**2
        if dist < min_dist or (dist == min_dist and (sr > target[0] if target else True or 
                             (sr == target[0] and sc > target[1]))):
            min_dist = dist
            target = (sr, sc, idx)
    
    return target

def move_santa_recursive(board, santas, cur, sr, sc, dr, dc, mul, N, alive):
    nr, nc = sr + dr * mul, sc + dc * mul
    
    if not (0 <= nr < N and 0 <= nc < N):
        alive[cur] = False
        return
        
    if board[nr][nc] == 0:  # 빈 칸
        board[nr][nc] = cur
        santas[cur] = [nr, nc]
    else:  # 다른 산타가 있는 경우
        next_santa = board[nr][nc]
        board[nr][nc] = cur
        santas[cur] = [nr, nc]
        move_santa_recursive(board, santas, next_santa, nr, nc, dr, dc, 1, N, alive)

def main():
    # 게임 초기화
    N, M, P, C, D, board, santas, scores, alive, wakeup_turn, rr, rc = init_game()
    
    # 게임 진행
    for turn in range(1, M+1):
        # 모든 산타가 탈락했는지 확인
        if not any(alive[1:]):
            break
            
        # 루돌프 이동
        target = get_closest_santa(rr, rc, santas, alive, N)
        if not target:
            break
            
        sr, sc, target_idx = target
        
        # 루돌프 이동 방향 결정
        rdr = (1 if sr > rr else -1) if sr != rr else 0
        rdc = (1 if sc > rc else -1) if sc != rc else 0
        
        # 루돌프 이동
        board[rr][rc] = 0
        rr, rc = rr + rdr, rc + rdc
        board[rr][rc] = -1
        
        # 충돌 체크
        if (rr, rc) == (sr, sc):
            scores[target_idx] += C
            wakeup_turn[target_idx] = turn + 2
            move_santa_recursive(board, santas, target_idx, sr, sc, rdr, rdc, C, N, alive)
            
        # 산타 이동
        for idx in range(1, P+1):
            if not alive[idx] or wakeup_turn[idx] > turn:
                continue
                
            sr, sc = santas[idx]
            best_move = None
            min_dist = (rr-sr)**2 + (rc-sc)**2
            
            # 이동 가능한 위치 탐색
            for dr, dc in [(-1,0), (0,1), (1,0), (0,-1)]:
                nr, nc = sr + dr, sc + dc
                if 0 <= nr < N and 0 <= nc < N and board[nr][nc] <= 0:
                    dist = (rr-nr)**2 + (rc-nc)**2
                    if dist < min_dist:
                        min_dist = dist
                        best_move = (nr, nc, dr, dc)
            
            if not best_move:
                continue
                
            nr, nc, dr, dc = best_move
            if (nr, nc) == (rr, rc):  # 루돌프와 충돌
                scores[idx] += D
                wakeup_turn[idx] = turn + 2
                board[sr][sc] = 0
                move_santa_recursive(board, santas, idx, nr, nc, -dr, -dc, D, N, alive)
            else:  # 일반 이동
                board[sr][sc] = 0
                board[nr][nc] = idx
                santas[idx] = [nr, nc]
        
        # 생존 산타 점수 증가
        for i in range(1, P+1):
            if alive[i]:
                scores[i] += 1
    
    # 결과 출력
    print(*scores[1:])

if __name__ == "__main__":
    main()