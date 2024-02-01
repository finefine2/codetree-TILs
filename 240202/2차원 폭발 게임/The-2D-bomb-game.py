# n, m, k = map(int, input().split())

# arr = []
# for i in range(n):
#     tmp = list(map(int, input().split()))
#     arr.append(tmp)

# def gravity():
#     for j in range(n):
#         col = []
#         for i in range(n):
#             if arr[i][j] != 0:
#                 col.append(arr[i][j])
#                 arr[i][j] = 0
#         for i in range(n - len(col), n):
#             arr[i][j] = col[i - (n - len(col))]

# def rotate():
#     global arr
#     new_arr = [[0] * n for _ in range(n)]

#     for i in range(n):
#         for j in range(n):
#             new_arr[i][j] = arr[j][n - 1 - i]

#     arr = new_arr
    
# # def rotate():
# #     global arr
# #     new_arr = [[0] * n for _ in range(n)]

    
# #     for i in range(n):
# #         for j in range(n):
# #             new_arr[i][j] = arr[j][n - 1 - i]
    
# #     for i in range(n):
# #         for j in range(n):
# #             arr[i][j] = new_arr[i][j]

# # def explode():
# #     check = False
# #     for j in range(n):
# #         cnt = 1
# #         for i in range(1, n):
# #             if arr[i][j] == arr[i-1][j] and arr[i][j] != 0:
# #                 cnt += 1
# #             else:
# #                 if cnt >= m:
# #                     for k in range(i - cnt, i):
# #                         arr[k][j] = 0
# #                     check = True
# #                 cnt = 1
        
# #         # 마지막 용
# #         if cnt >= m:
# #             for k in range(n - cnt, n):
# #                 arr[k][j] = 0
# #             check = True

# #     return check

# def explode():
#     exploded = False
#     mark = [[False] * n for _ in range(n)]  # 폭발할 위치를 표시하기 위한 배열

#     # 각 열별로 연속된 숫자들이 m개 이상 있는지 확인
#     for j in range(n):
#         i = 0
#         while i < n:
#             if arr[i][j] == 0:
#                 i += 1
#                 continue
#             start = i
#             while i < n and arr[start][j] == arr[i][j]:
#                 i += 1
#             if i - start >= m:
#                 for k in range(start, i):
#                     mark[k][j] = True
#                 exploded = True
    
#     # 폭발할 위치의 숫자를 0으로 변경
#     for i in range(n):
#         for j in range(n):
#             if mark[i][j]:
#                 arr[i][j] = 0

#     return exploded


# # for _ in range(k):
# #     if not explode():
# #         break
# #     gravity()
# #     rotate()
# for _ in range(k):
#     exploded = explode()
#     gravity()

#     if not exploded:
#         break

#     rotate()



# ans = 0
# for i in range(n):
#     for j in range(n):
#         if arr[i][j] != 0:
#             ans += 1

# print(ans)



# 계속 한시간 넘게 45% 쯤에서 안되서 코드를 구글링해서 참조해서 내버렸다....
            
def get_exploded_x(y):
    exploded_x = []
    x = 0
    counts = 0
    standard = board[x][y]

    while x < n:
        if board[x][y] == 0:
            x += 1
            if x < n:
                standard = board[x][y]
            continue

        if standard == board[x][y]:
            x += 1
            counts += 1
        else:
            if m <= counts:
                for i in range(x - counts, x):
                    exploded_x.append(i)

            standard = board[x][y]
            counts = 0

    if m <= counts:
        for i in range(n - counts, n):
            exploded_x.append(i)

    return exploded_x


def line_explode(exploded_x, y):
    for x in exploded_x:
        board[x][y] = 0


def drop(y):
    temp = [board[x][y] for x in range(n) if board[x][y] > 0]
    i = 0

    for x in range(n):
        if x < n - len(temp):
            board[x][y] = 0
        else:
            board[x][y] = temp[i]
            i += 1


def bomb():
    for y in range(n):
        while True:
            exploded_x = get_exploded_x(y)

            if not exploded_x:
                break

            line_explode(exploded_x, y)
            drop(y)


def rotate():
    global board
    board = [list(line[::-1]) for line in zip(*board)]


n, m, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

for _ in range(k):
    bomb()
    rotate()
    for y in range(n):
        drop(y)

bomb()

print(sum(board[x][y] > 0 for x in range(n) for y in range(n)))