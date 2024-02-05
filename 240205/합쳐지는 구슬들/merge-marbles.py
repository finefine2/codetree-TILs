# n, m, t = map(int, input().split())

# arr = [[[] for _ in range(n)] for _ in range(n)]

# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
# dir = {'U': 0, 'D': 1, 'L': 2, 'R': 3}

# def isin(a, b):
#     return 0<=a<n and 0<=b<n

# for i in range(m):
#     r, c, d, v = map(str, input().split())
#     r = int(r) - 1
#     c = int(c) - 1
#     v = int(v)
#     arr[r][c].append([i, d, v])
#     # 번호와 방향 속도를 arr[r][c]에 넣어준다.


# for _ in range(t):
#     move = [[[] for _ in range(n)] for _ in range(n)]

#     for i in range(n):
#         for j in range(n):
#             for ball in range(len(arr[i][j])):  # ball 번째 구슬
#                 bx, by = i, j
#                 moving = 0

#                 while moving < arr[i][j][ball][2]:
#                     nx = bx + dx[dir[arr[i][j][ball][1]]]  
#                     ny = by + dy[dir[arr[i][j][ball][1]]]
#                     # [i][j][ball][1]은 방향을 나타내므로 그거에 따라 이동

#                     if isin(nx, ny):
#                         moving += 1
#                         if moving == arr[i][j][ball][2]:
#                             move[nx][ny].append(arr[i][j][ball])
#                         bx, by = nx, ny

#                     else:  # 나갈 경우에는 방향이 반대로 바뀐다.
#                         if arr[i][j][ball][1] == 'U':
#                             arr[i][j][ball][1] = 'D'
#                         elif arr[i][j][ball][1] == 'D':
#                             arr[i][j][ball][1] = 'U'
#                         elif arr[i][j][ball][1] == 'L':
#                             arr[i][j][ball][1] = 'R'
#                         else:
#                             arr[i][j][ball][1] = 'L'

#     for i in range(n):
#         for j in range(n):
#             while len(move[i][j]) > 1:   # 구슬 수를 넘었을 때
#                 MinV = 11
#                 MinB = -1

#                 for l in range(len(move[i][j])):
#                     if move[i][j][l][2] < MinV:   # 더 작은 값이 있을때 갱신
#                         MinV = move[i][j][l][2]
#                         MinB = l 
#                     elif move[i][j][l][2] == MinV:
#                         if move[i][j][MinB][0] > move[i][j][l][0]:
#                             MinB = l 
                
#                 move[i][j].pop(MinB)

#             arr[i][j] = move[i][j]


# ans = 0
# for i in range(n):
#     for j in range(n):
#         print(arr[i][j], end = " ")
#     print()

# print(ans)

n, m, t = map(int, input().split())

# 구슬의 정보를 담을 리스트, 구슬 번호(i+1), 방향, 무게를 저장
balls = []
for i in range(m):
    r, c, d, w = input().split()
    r, c, w = int(r)-1, int(c)-1, int(w)
    balls.append([r, c, d, w, i+1])  # 위치, 방향, 무게, 번호

dir = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
def isin(a, b):
    return 0<=a<n and 0<=b<n

for _ in range(t):
    new_positions = {}

    for ball in balls:
        r, c, d, w, num = ball
        dr, dc = dir[d]
        nr, nc = r + dr, c + dc

        if not isin(nr,nc):
            if d == 'U': d = 'D'
            elif d == 'D': d = 'U'
            elif d == 'L': d = 'R'
            elif d == 'R': d = 'L'

            nr, nc = r + dir[d][0], c + dir[d][1]

        ball[0], ball[1], ball[2] = nr, nc, d  # 위치와 방향 업데이트

        key = (nr, nc)
        if key not in new_positions:
            new_positions[key] = []

        new_positions[key].append([nr, nc, d, w, num])

    # 충돌 처리
    balls = []
    for pos in new_positions:
        if len(new_positions[pos]) > 1:

            # 충돌하여 합쳐지는 구슬 처리
            sum_biz = 0
            for ball in new_positions[pos]:
                sum_biz += ball[3]

            max_num = max(new_positions[pos], key=lambda x: x[4])
            # 가장 큰 번호를 가진 구슬 찾기

            balls.append([pos[0], pos[1], max_num[2], sum_biz, max_num[4]])
        else:
            balls.append(new_positions[pos][0])
            # 1개 이하일 경우 추가해준다.


if balls:
    ans = max(balls, key=lambda x: x[3])[3]
else:
    ans = 0

print(len(balls), ans)