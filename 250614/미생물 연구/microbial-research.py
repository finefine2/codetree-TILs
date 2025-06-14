def solve_microbial_research():
    # 방향 벡터 (상, 하, 좌, 우)
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    
    def dfs_mark_component(board, visited, y, x, micro_id, n):
        visited[y][x] = True
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if (0 <= ny < n and 0 <= nx < n and 
                not visited[ny][nx] and 
                board[ny][nx] == micro_id):
                dfs_mark_component(board, visited, ny, nx, micro_id, n)
    
    def arrange_microorganisms(current_board, micro_id, r1, c1, r2, c2, n):
        visited = [[False] * n for _ in range(n)]
        connected_component_count = [0] * (micro_id + 1)
        
        # 미생물 주입
        for row in range(r1, r2):
            for col in range(c1, c2):
                current_board[row][col] = micro_id
        
        # 연결 성분 개수 확인
        for row in range(n):
            for col in range(n):
                if current_board[row][col] != 0 and not visited[row][col]:
                    current_micro_id = current_board[row][col]
                    connected_component_count[current_micro_id] += 1
                    dfs_mark_component(current_board, visited, row, col, current_micro_id, n)
        
        # 분리된 미생물 제거
        for micro_id_to_check in range(1, micro_id + 1):
            if connected_component_count[micro_id_to_check] >= 2:
                for row in range(n):
                    for col in range(n):
                        if current_board[row][col] == micro_id_to_check:
                            current_board[row][col] = 0
    
    def get_microorganism_bounds(board, micro_id, n):
        min_r, max_r = n, -1
        min_c, max_c = n, -1
        area = 0
        
        for row in range(n):
            for col in range(n):
                if board[row][col] == micro_id:
                    min_r = min(min_r, row)
                    max_r = max(max_r, row)
                    min_c = min(min_c, col)
                    max_c = max(max_c, col)
                    area += 1
        
        return {'min_r': min_r, 'max_r': max_r, 'min_c': min_c, 'max_c': max_c, 'area': area} if area > 0 else None
    
    def can_place_microorganism(board, bounds, target_r, target_c, n):
        width = bounds['max_c'] - bounds['min_c'] + 1
        height = bounds['max_r'] - bounds['min_r'] + 1
        
        if target_r + height > n or target_c + width > n:
            return False
        
        for dr in range(height):
            for dc in range(width):
                if board[target_r + dr][target_c + dc] != 0:
                    return False
        return True
    
    def relocate_microorganisms(current_board, experiment_id, n):
        new_board = [[0] * n for _ in range(n)]
        
        for micro_id in range(1, experiment_id + 1):
            bounds = get_microorganism_bounds(current_board, micro_id, n)
            if bounds is None:
                continue
            
            placed = False
            for target_r in range(n):
                for target_c in range(n):
                    if can_place_microorganism(new_board, bounds, target_r, target_c, n):
                        width = bounds['max_c'] - bounds['min_c'] + 1
                        height = bounds['max_r'] - bounds['min_r'] + 1
                        
                        for dr in range(height):
                            for dc in range(width):
                                orig_r = bounds['min_r'] + dr
                                orig_c = bounds['min_c'] + dc
                                if current_board[orig_r][orig_c] == micro_id:
                                    new_board[target_r + dr][target_c + dc] = micro_id
                        placed = True
                        break
                if placed:
                    break
        
        return new_board
    
    def calculate_experiment_result(board, experiment_id, n):
        areas = {}
        for micro_id in range(1, experiment_id + 1):
            bounds = get_microorganism_bounds(board, micro_id, n)
            if bounds:
                areas[micro_id] = bounds['area']
        
        adjacent_pairs = set()
        for row in range(n):
            for col in range(n):
                if board[row][col] != 0:
                    current_id = board[row][col]
                    for i in range(4):
                        ny, nx = row + dy[i], col + dx[i]
                        if (0 <= ny < n and 0 <= nx < n and 
                            board[ny][nx] != 0 and 
                            board[ny][nx] != current_id):
                            pair = tuple(sorted([current_id, board[ny][nx]]))
                            adjacent_pairs.add(pair)
        
        total_score = 0
        for pair in adjacent_pairs:
            id1, id2 = pair
            if id1 in areas and id2 in areas:
                total_score += areas[id1] * areas[id2]
        
        return total_score
    
    # 메인 실행 부분
    n, q = map(int, input().split())
    current_board = [[0] * n for _ in range(n)]
    
    for experiment_id in range(1, q + 1):
        r1, c1, r2, c2 = map(int, input().split())
        
        # 1단계: 미생물 주입과 분리된 미생물 무리의 제거
        arrange_microorganisms(current_board, experiment_id, r1, c1, r2, c2, n)
        
        # 2단계: 미생물의 배양 용기 이동
        current_board = relocate_microorganisms(current_board, experiment_id, n)
        
        # 3단계: 실험 결과 계산
        score = calculate_experiment_result(current_board, experiment_id, n)
        print(score)

# 실행
solve_microbial_research()
