N = 19
board = [list(map(int, input().split())) for _ in range(N)]


def in_range(x, y):
    return 0 <= x and x < N and 0 <= y and y < N


def check_win(x, y, dx, dy, current):
    for k in range(1, 5):
        nx, ny = x + k * dx, y + k * dy
        if not in_range(nx, ny) or board[nx][ny] != current:
            return False
    
    return True


def find_winner():
    for x in range(N):
        for y in range(N):
            if board[x][y] == 1 or board[x][y] == 2:
                dxs, dys = [0, 1, 1, 1], [1, 0, 1, -1]
                for dx, dy in zip(dxs, dys):
                    if check_win(x, y, dx, dy, board[x][y]):
                        return board[x][y], x + dx * 2, y + dy * 2
    
    return 0, None, None


winner, x, y = find_winner()
if winner:
    print(winner)
    print(x + 1, y + 1)
else:
    print(0)