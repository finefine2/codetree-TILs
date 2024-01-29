n = int(input())

arr = []
for i in range(n):
    st = list(map(int, input().split()))
    arr.append(st)

# ans = 0
# for i in range(1, n-1):
#     for j in range(1, n-1):
#         s = 0
#         s -= arr[i][j]
#         ax, ay = 0, 0
#         bx, by = 0, 0
#         cx, cy = 0, 0
#         dx, dy = 0, 0
#         for x in range(n):
#             for y in range(n):
#                 if x + y == i + j:
#                     s += arr[x][y]
#                     ax = x
#                     ay = y
#         for x in range(n):
#             for y in range(n):
#                 if abs(ax - ay) == abs(x - y) and x != ax and y != ay:
#                     s += arr[x][y]
#                     bx = x
#                     by = y
#         for x in range(n):
#             for y in range(n):
#                 if x + y == bx + by and x != bx and y != by:
#                     s += arr[x][y]
#                     cx = x
#                     cy = y
#         for x in range(n):
#             for y in range(n):
#                 if abs(cx - cy) == abs(x - y) and x != cx and y != cy:
#                     s += arr[x][y]
#                     dx = x
#                     dy = y
#         s -= arr[ax][ay]
#         s -= arr[bx][by]
#         s -= arr[cx][cy]
#         print(ax, ay, bx, by, cx, cy, dx, dy)
#         print(s)
#         ans = max(ans, s)

# print(ans)        

dy=[-1, -1, 1, 1]
dx=[1, -1, -1, 1]

def square(x,y,a,b):
    num = 0
    turn = [a, b, a, b]
    for i in range(4):
        for j in range(turn[i]):
            x += dx[i]
            y += dy[i]
            if x < 0 or x >= n or y < 0 or y >= n:
                return 0
            num += arr[x][y]
    return num
        # if i % 2 == 0:
        #     for j in range(a):
            #     x += dx[i]
            #     y += dy[i]
            #     # if x < 0 or x >= n or y < 0 or y >= n:
            #     #     return 0
            #     if not(0<=y<n and 0<=x<n):
            #         return 0
            #     num += arr[y][x]
            # return num
        # else:
        #     for j in range(b):
        #         x += dx[i]
        #         y += dy[i]
        #         # if x < 0 or x >= n or y < 0 or y >= n:
        #         #     return 0
        #         if not(0<=y<n and 0<=x<n):
        #             return 0
        #         num += arr[y][x]
        #     return num

ans = []
for i in range(n):
    for j in range(n):
        for k in range(1, n):
            for l in range(1, n):
                ans.append(square(i, j, k, l))

print(max(ans))

# ans = []
# for i in range(n):
#     for j in range(n):
#         for k in range(1, n):
#             for l in range(1, n):
#                 num = 0
#                 flag = False
#                 for ii in range(4):
#                     if ii % 2 == 0:
#                         for jj in range(k):
#                             x = i + dx[ii]
#                             y = j + dy[ii]
#                             if x < 0 or x >= n or y < 0 or y >= n:
#                                 num = 0
#                                 flag = True
#                                 break
#                             else:
#                                 num += arr[x][y]
#                     else:
#                         for jj in range(l):
#                             x = i + dx[ii]
#                             y = j + dy[ii]
#                             if x < 0 or x >= n or y < 0 or y >= n:
#                                 num = 0
#                                 flag = True
#                                 break
#                             else:
#                                 num += arr[x][y]
#                 if flag:
#                     ans.append(0)
#                 else:
#                     ans.append(num)

# print(max(ans))   

# (0,0) (0,1) (0,2) (0,3)
# (1,0) (1,1) (1,2) (1,3)
# (2,0) (2,1) (2,2) (2,3)
# (3,0) (3,1) (3,2) (3,3)