from collections import deque

N, M = map(int, input().split())
board = [[-1] * (N + 2)] + [[-1] + list(map(int, input().split())) + [-1] for _ in range(N)] + [[-1] * (N + 2)]
EMPTY = M + 1


def get_base(group):
    """기준 블록 찾기 (가장 아래, 가장 왼쪽)"""
    base_r, base_c = -1, N + 1
    for r, c in group:
        if board[r][c] != 0:  # 빨간색이 아닌 블록
            if r > base_r or (r == base_r and c < base_c):
                base_r, base_c = r, c
    return base_r, base_c


def bfs(sr, sc, visited):
    """시작점에서 같은 색 폭탄 그룹 찾기"""
    if visited[sr][sc] or not (0 < board[sr][sc] <= M):
        return set()

    q = deque([(sr, sc)])
    group = set([(sr, sc)])
    red_cnt = 0
    color = board[sr][sc]
    visited[sr][sc] = 1

    while q:
        cr, cc = q.popleft()
        for nr, nc in [(cr - 1, cc), (cr, cc + 1), (cr + 1, cc), (cr, cc - 1)]:
            if (not visited[nr][nc] and
                    (nr, nc) not in group and
                    (board[nr][nc] == color or board[nr][nc] == 0)):
                q.append((nr, nc))
                group.add((nr, nc))
                if board[nr][nc] == 0:
                    red_cnt += 1
                else:
                    visited[nr][nc] = 1

    if len(group) < 2:  # 크기가 2 미만이면 무시
        return set()

    base_r, base_c = get_base(group)
    return (len(group), red_cnt, base_r, base_c, group)


def find_largest_group():
    """가장 큰 폭탄 그룹 찾기"""
    visited = [[0] * (N + 2) for _ in range(N + 2)]
    max_group = None

    for r in range(1, N + 1):
        for c in range(1, N + 1):
            if not visited[r][c] and 0 < board[r][c] <= M:
                result = bfs(r, c, visited)
                if result:
                    if not max_group or result[:4] > max_group[:4]:
                        max_group = result

    return max_group[-1] if max_group else set()


def gravity():
    """중력 적용"""
    for sr in range(1, N):
        for sc in range(1, N + 1):
            cr, cc = sr, sc
            while 0 <= board[cr][cc] <= M and board[cr + 1][cc] == EMPTY:
                board[cr][cc], board[cr + 1][cc] = board[cr + 1][cc], board[cr][cc]
                cr -= 1


def rotate():
    """반시계 방향 90도 회전"""
    global board
    board = list(map(list, zip(*board)))[::-1]


# 메인 로직
ans = 0
while True:
    # 가장 큰 폭탄 그룹 찾기
    bomb_group = find_largest_group()

    # 종료 조건: 크기가 2 미만인 그룹만 있는 경우
    if len(bomb_group) < 2:
        break

    # 점수 계산
    ans += len(bomb_group) ** 2

    # 폭탄 제거
    for br, bc in bomb_group:
        board[br][bc] = EMPTY

    # 중력 적용
    gravity()

    # 회전 후 중력 적용
    rotate()
    gravity()

print(ans)