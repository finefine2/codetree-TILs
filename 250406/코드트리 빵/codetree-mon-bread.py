from collections import deque

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

# 베이스캠프와 편의점 위치 저장
stores = []  # 편의점 위치
camps = []   # 베이스캠프 위치

for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            camps.append((i, j))

for _ in range(m):
    r, c = map(int, input().split())
    stores.append((r-1, c-1))  # 0-based index로 변환

def in_range(r, c):
    return 0 <= r < n and 0 <= c < n

def find_shortest_path(sr, sc, er, ec, blocked):
    """
    (sr,sc)에서 (er,ec)까지의 최단 경로를 찾는 BFS
    blocked: 이미 막힌 위치들의 집합
    """
    if (sr, sc) == (er, ec):
        return None
        
    q = deque([(sr, sc)])
    visited = [[False] * n for _ in range(n)]
    parent = {}  # 경로 추적을 위한 부모 노드 저장
    
    visited[sr][sc] = True
    
    while q:
        r, c = q.popleft()
        
        # 4방향 탐색 (상좌우하 우선순위)
        for dr, dc in [(-1,0), (0,-1), (0,1), (1,0)]:
            nr, nc = r + dr, c + dc
            
            if not in_range(nr, nc):
                continue
            if (nr, nc) in blocked:
                continue
            if visited[nr][nc]:
                continue
                
            visited[nr][nc] = True
            q.append((nr, nc))
            parent[(nr, nc)] = (r, c)
            
            if (nr, nc) == (er, ec):
                # 경로 역추적
                path = []
                curr = (nr, nc)
                while curr in parent:
                    path.append(curr)
                    curr = parent[curr]
                path.append((sr, sc))
                return path[::-1]
    
    return None

def find_nearest_basecamp(store_r, store_c, blocked):
    """
    특정 편의점에서 가장 가까운 베이스캠프를 찾는 BFS
    """
    q = deque([(store_r, store_c, 0)])
    visited = [[False] * n for _ in range(n)]
    visited[store_r][store_c] = True
    
    min_dist = float('inf')
    candidates = []
    
    while q:
        r, c, dist = q.popleft()
        
        if dist > min_dist:
            break
            
        if board[r][c] == 1 and (r, c) not in blocked:
            min_dist = dist
            candidates.append((r, c))
            continue
            
        for dr, dc in [(-1,0), (0,-1), (0,1), (1,0)]:
            nr, nc = r + dr, c + dc
            
            if not in_range(nr, nc):
                continue
            if visited[nr][nc]:
                continue
                
            visited[nr][nc] = True
            q.append((nr, nc, dist + 1))
    
    if not candidates:
        return None
    
    # 가장 위쪽, 왼쪽 베이스캠프 선택
    return min(candidates)

def simulate():
    time = 0
    blocked = set()  # 이미 사용된 공간
    people = {}      # 현재 이동 중인 사람들 {사람번호: 현재위치}
    arrived = set()  # 도착한 사람들
    
    while len(arrived) < m:
        # 1. 모든 사람이 한 칸씩 이동
        new_people = {}
        for person, pos in people.items():
            if person in arrived:
                continue
                
            path = find_shortest_path(pos[0], pos[1], 
                                    stores[person][0], stores[person][1], 
                                    blocked)
            if path and len(path) > 1:
                new_people[person] = path[1]
            else:
                new_people[person] = pos
                
            # 편의점 도착 체크
            if new_people[person] == stores[person]:
                arrived.add(person)
                blocked.add(stores[person])
        
        people = new_people
        
        # 2. 새로운 사람 출발 (시간이 사람 번호보다 크거나 같을 때)
        if time < m:
            store = stores[time]
            camp = find_nearest_basecamp(store[0], store[1], blocked)
            if camp:
                people[time] = camp
                blocked.add(camp)
        
        time += 1
        
    return time

print(simulate())