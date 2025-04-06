from collections import deque

def process_eggs(n, l, r, eggs):
    def valid_range(x, y):
        return 0 <= x < n and 0 <= y < n

    def can_share(x1, y1, x2, y2):
        diff = abs(eggs[x1][y1] - eggs[x2][y2])
        return l <= diff <= r

    def bfs(start_x, start_y, visited):
        q = deque([(start_x, start_y)])
        group = [(start_x, start_y)]
        visited[start_x][start_y] = True
        total = eggs[start_x][start_y]
        
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        
        while q:
            x, y = q.popleft()
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if valid_range(nx, ny) and not visited[nx][ny]:
                    if can_share(x, y, nx, ny):
                        visited[nx][ny] = True
                        q.append((nx, ny))
                        group.append((nx, ny))
                        total += eggs[nx][ny]
        
        # 그룹이 형성되면 평균값으로 업데이트
        if len(group) > 1:
            avg = total // len(group)
            return group, avg
        return None

    time = 0
    while True:
        visited = [[False] * n for _ in range(n)]
        changes = []
        
        # 모든 위치에서 BFS 시도
        for i in range(n):
            for j in range(n):
                if not visited[i][j]:
                    result = bfs(i, j, visited)
                    if result:
                        changes.append(result)
        
        # 더 이상 변화가 없으면 종료
        if not changes:
            break
            
        # 모든 변화를 동시에 적용
        for group, avg in changes:
            for x, y in group:
                eggs[x][y] = avg
                
        time += 1
    
    return time

# 입력 처리
n, l, r = map(int, input().split())
eggs = [list(map(int, input().split())) for _ in range(n)]

# 결과 출력
print(process_eggs(n, l, r, eggs))