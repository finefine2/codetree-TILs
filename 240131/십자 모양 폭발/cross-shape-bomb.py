import copy
n = int(input())

arr = []
for i in range(n):
    tmp = list(map(int, input().split()))
    arr.append(tmp)

# check = [[0] * n for _ in range(n)]

r, c = map(int, input().split())

arr2 = copy.deepcopy(arr)
r -= 1
c -= 1
m = arr[r][c]

dx = [0,0,1,-1]
dy = [1,-1,0,0]

arr2[r][c] = 0
for i in range(4):
    for j in range(1, m):
        nx = r + dx[i] * j
        ny = c + dy[i] * j
        
        if 0<=nx<n and 0<=ny<n:
            arr2[nx][ny] = 0
        else:
            break


# for i in range(n):
#     for j in range(n):
#         print(arr2[i][j], end = " ")
#     print()

# print()

# for j in range(n):
#     empty_cnt = 0
#     for i in range(n-1, 0, -1):
#         if arr2[i][j] == 0:
#             empty_cnt += 1
#         else:
#             arr2[i+empty_cnt][j] = arr2[i][j]
#             if empty_cnt > 0:
#                 arr2[i][j] = 0

# 중력 부분 수정
for j in range(n):
    for i in range(n-1, 0, -1):
        if arr2[i][j] == 0:
            k = i - 1
            while k >= 0 and arr2[k][j] == 0:
                k -= 1
            if k >= 0:
                arr2[i][j] = arr2[k][j]
                arr2[k][j] = 0

# for j in range(n):
#     for i in range(n-1, 0, -1):
#         if arr2[i][j] == 0:
#             k = i
#             tmp = 0
#             while k > 0 and arr2[k][j] == 0:
#                 # if k == 0:
#                 #     break
#                 arr2[k][j], arr2[k-1][j] = arr2[k-1][j], arr2[k][j]
#                 # tmp = arr2[k][j]
#                 # arr2[k][j] = arr2[k-1][j]
#                 # arr2[k-1][j] = tmp
#                 k -= 1

for i in range(n):
    for j in range(n):
        print(arr2[i][j], end = " ")
    print()