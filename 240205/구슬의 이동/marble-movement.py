n, m, t, k = map(int, input().split())

arr = [[[] for _ in range(n)] for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
dir = {'U': 0, 'D': 1, 'L': 2, 'R': 3}

def isin(a, b):
    return 0<=a<n and 0<=b<n

for i in range(m):
    r, c, d, v = map(str, input().split())
    r = int(r) - 1
    c = int(c) - 1
    v = int(v)
    arr[r][c].append([i, d, v])
    # 번호와 방향 속도를 arr[r][c]에 넣어준다.


for _ in range(t):
    move = [[[] for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            for ball in range(len(arr[i][j])):  # ball 번째 구슬
                bx, by = i, j
                moving = 0

                while moving < arr[i][j][ball][2]:
                    nx = bx + dx[dir[arr[i][j][ball][1]]]  
                    ny = by + dy[dir[arr[i][j][ball][1]]]
                    # [i][j][ball][1]은 방향을 나타내므로 그거에 따라 이동

                    if isin(nx, ny):
                        moving += 1
                        if moving == arr[i][j][ball][2]:
                            move[nx][ny].append(arr[i][j][ball])
                        bx, by = nx, ny

                    else:  # 나갈 경우에는 방향이 반대로 바뀐다.
                        if arr[i][j][ball][1] == 'U':
                            arr[i][j][ball][1] = 'D'
                        elif arr[i][j][ball][1] == 'D':
                            arr[i][j][ball][1] = 'U'
                        elif arr[i][j][ball][1] == 'L':
                            arr[i][j][ball][1] = 'R'
                        else:
                            arr[i][j][ball][1] = 'L'

    for i in range(n):
        for j in range(n):
            while len(move[i][j]) > k:   # 구슬 수를 넘었을 때
                MinV = 11
                MinB = -1

                for l in range(len(move[i][j])):
                    if move[i][j][l][2] < MinV:   # 더 작은 값이 있을때 갱신
                        MinV = move[i][j][l][2]
                        MinB = l 
                    elif move[i][j][l][2] == MinV:
                        if move[i][j][MinB][0] > move[i][j][l][0]:
                            MinB = l 
                
                move[i][j].pop(MinB)

            arr[i][j] = move[i][j]


ans = 0
for i in range(n):
    for j in range(n):
        ans += len(arr[i][j])

print(ans)