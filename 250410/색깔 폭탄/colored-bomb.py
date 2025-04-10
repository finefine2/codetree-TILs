N, M = map(int, input().split())

EMPTY = M + 1
RED = 0
board = [[-1] * (N + 2)] + [[-1] + list(map(int, input().split())) + [-1] for _ in range(N)] + [[-1] * (N + 2)]

from collections import deque


def bfs(sr, sc, v):
    q = deque()
    group = set()

    color = board[sr][sc]
    q.append((sr, sc))
    group.add((sr, sc))
    v[sr][sc] = 1

    r_cnt = 0
    normal_cnt = 1  # 일반 블록 카운트

    while q:
        cr, cc = q.popleft()
        for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nr, nc = cr + dr, cc + dc
            if v[nr][nc] == 0 and (nr, nc) not in group and (board[nr][nc] == color or board[nr][nc] == RED):
                q.append((nr, nc))
                group.add((nr, nc))
                if board[nr][nc] == RED:
                    r_cnt += 1
                else:
                    normal_cnt += 1
                    v[nr][nc] = 1

    # 빨간색 폭탄만으로 이루어진 그룹이거나 크기가 2 미만인 경우 제외
    if normal_cnt == 0 or len(group) < 2:
        return None

    base_r, base_c = get_base(group)
    return (len(group), r_cnt, base_r, base_c, group)


def gravity():
    global board
    for c in range(1, N + 1):
        empty = N
        for r in range(N, 0, -1):
            if board[r][c] == -1:
                empty = r - 1
            elif board[r][c] != EMPTY:
                if r != empty:
                    board[empty][c] = board[r][c]
                    board[r][c] = EMPTY
                empty -= 1


def get_base(group):
    max_r, min_c = -1, N + 1
    for gr, gc in group:
        if board[gr][gc] != RED:
            if gr > max_r or (gr == max_r and min_c > gc):
                max_r, min_c = gr, gc
    return max_r, min_c


ans = 0

while True:
    v = [[0] * (N + 2) for _ in range(N + 2)]
    max_group = None

    # 모든 위치에서 가능한 폭탄 그룹을 찾고, 그 중 가장 큰 그룹 선택
    for sr in range(1, N + 1):
        for sc in range(1, N + 1):
            if v[sr][sc] == 0 and 0 < board[sr][sc] <= M:
                result = bfs(sr, sc, v)
                if result:
                    if not max_group or result[:4] > max_group[:4]:
                        max_group = result

    if not max_group:
        break

    bomb_group = max_group[4]
    ans += len(bomb_group) ** 2

    # 폭탄 제거
    for br, bc in bomb_group:
        board[br][bc] = EMPTY

    # 중력 적용
    gravity()

    # 반시계 90도 회전
    board = list(map(list, zip(*board)))[::-1]

    # 다시 중력 적용
    gravity()

print(ans)