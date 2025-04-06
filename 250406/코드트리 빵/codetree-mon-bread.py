from collections import deque

def init():
    N, M = map(int, input().split())
    # 패딩된 보드 생성
    board = [[1] * (N+2)] + [[1] + list(map(int, input().split())) + [1] 
            for _ in range(N)] + [[1] * (N+2)]
    
    # 베이스캠프와 편의점 정보 저장
    basecamp = set()
    for r in range(1, N+1):
        for c in range(1, N+1):
            if board[r][c] == 1:
                basecamp.add((r, c))
                board[r][c] = 0
    
    stores = {}
    for m in range(1, M+1):
        r, c = map(int, input().split())
        stores[m] = (r, c)
    
    return N, M, board, basecamp, stores

def find_nearest(sr, sc, dests, board, N):
    """최단 거리의 목적지들을 찾는 BFS"""
    drs, dcs = [-1, 0, 0, 1], [0, -1, 1, 0]
    q = deque([(sr, sc)])
    visited = [[False] * (N+2) for _ in range(N+2)]
    visited[sr][sc] = True
    
    while q:
        candidates = []
        size = len(q)  # 현재 레벨의 크기
        
        # 현재 레벨의 모든 노드 처리
        for _ in range(size):
            cr, cc = q.popleft()
            if (cr, cc) in dests:
                candidates.append((cr, cc))
            else:
                for dr, dc in zip(drs, dcs):
                    nr, nc = cr + dr, cc + dc
                    if not visited[nr][nc] and board[nr][nc] == 0:
                        visited[nr][nc] = True
                        q.append((nr, nc))
        
        # 현재 레벨에서 목적지를 찾았다면 가장 우선순위가 높은 것 반환
        if candidates:
            return min(candidates)  # 정렬 대신 min 사용
    return -1

def solve(N, M, board, basecamp, stores):
    people = deque()  # (r, c, person_num)
    arrived = [0] * (M + 1)
    time = 1
    
    while people or time <= M:
        # 1. 이동 처리
        next_people = deque()
        arrived_positions = []
        
        for cr, cc, person in people:
            if arrived[person]:
                continue
                
            sr, sc = stores[person]
            next_pos = find_nearest(sr, sc, 
                                  {(cr-1,cc), (cr+1,cc), (cr,cc-1), (cr,cc+1)},
                                  board, N)
            
            if next_pos == (sr, sc):  # 편의점 도착
                arrived[person] = time
                arrived_positions.append(next_pos)
            else:
                next_people.append((next_pos[0], next_pos[1], person))
        
        people = next_people
        
        # 2. 도착 처리
        for r, c in arrived_positions:
            board[r][c] = 1
        
        # 3. 새로운 사람 베이스캠프 배치
        if time <= M:
            sr, sc = stores[time]
            camp_pos = find_nearest(sr, sc, basecamp, board, N)
            basecamp.remove(camp_pos)
            board[camp_pos[0]][camp_pos[1]] = 1
            people.append((camp_pos[0], camp_pos[1], time))
        
        time += 1
    
    return max(arrived)

def main():
    N, M, board, basecamp, stores = init()
    print(solve(N, M, board, basecamp, stores))

if __name__ == "__main__":
    main()