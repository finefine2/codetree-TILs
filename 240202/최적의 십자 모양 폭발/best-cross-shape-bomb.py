import copy
n = int(input())

arr = []
for i in range(n):
    tmp = list(map(int, input().split()))
    arr.append(tmp)

def gravity(arr2):
    for j in range(n):
        col = []
        for i in range(n):
            if arr2[i][j] != 0:
                col.append(arr[i][j])
                arr2[i][j] = 0
        for i in range(n - len(col), n):
            arr2[i][j] = col[i - (n - len(col))]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def explode(arr2, x, y):
    num = arr2[x][y]
    arr2[x][y] = 0
    for dir in range(4):
        for i in range(1, num):
            nx = x + dx[dir] * i
            ny = y + dy[dir] * i
        
            if 0 <= nx < n and 0 <= ny < n:
                arr2[nx][ny] = 0

Max = 0
for i in range(n):
    for j in range(n):
        arr2 = copy.deepcopy(arr)
        explode(arr2, i, j)
        
        gravity(arr2)
        # for i in range(n):
        #     for j in range(n):
        #         print(arr2[i][j], end = " ")
        #     print()
        # print()

        ans = 0
        for k in range(n):
            for l in range(n-1):  # 오른쪽 인접 쌍 확인
                if arr2[k][l] == arr2[k][l+1] and arr2[k][l] != 0:
                    ans += 1
            for l in range(n):  # 아래쪽 인접 쌍 확인
                if k < n-1 and arr2[k][l] == arr2[k+1][l] and arr2[k][l] != 0:
                    ans += 1
                    
        Max = max(ans, Max)

print(Max)

# Max = 0
# for i in range(n):

#     for j in range(n):
#         arr2 = copy.deepcopy(arr)
#         explode(arr2, i, j)
#         gravity()

#         ans = 0
#         for k in range(n):
#             for l in range(n):
#                 if k == 0 and l == 0:
#                     if arr2[k][l] == arr2[k+1][l]:
#                         ans += 1
#                     elif arr2[k][l] == arr2[k][l+1]:
#                         ans += 1
#                 elif k == n-1 and l == 0:
#                     if arr2[k][l] == arr2[k][l+1]:
#                         ans += 1
#                     elif arr2[k][l] == arr2[k-1][l]:
#                         ans += 1
#                 elif k == 0 and l == n-1:
#                     if arr2[k][l] == arr2[k][l-1]:
#                         ans += 1
#                     elif arr2[k][l] == arr2[k+1][l]:
#                         ans += 1
#                 elif l == 0 and k+1 < n:
#                     if arr2[k][l] == arr2[k-1][l]:
#                         ans += 1
#                     elif arr2[k][l] == arr2[k][l+1]:
#                         ans += 1
#                     elif arr2[k][l] == arr2[k+1][l]:
#                         ans += 1
#                 elif k == 0 and l+1 < n:
#                     if arr2[k][l] == arr2[k+1][l]:
#                         ans += 1
#                     elif arr2[k][l] == arr2[k][l-1]:
#                         ans += 1
#                     elif arr2[k][l] == arr2[k][l+1]:
#                         ans += 1
#                 elif l == n-1 and k+1 < n:
#                     if arr2[k][l] == arr2[k+1][l]:
#                         ans += 1
#                     elif arr2[k][l] == arr2[k][l-1]:
#                         ans += 1
#                     elif arr2[k][l] == arr2[k-1][l]:
#                         ans += 1
#                 elif k == n-1 and l+1 < n:
#                     if arr2[k][l] == arr2[k][l+1]:
#                         ans += 1
#                     elif arr2[k][l] == arr2[k][l-1]:
#                         ans += 1
#                     elif arr2[k][l] == arr2[k-1][l]:
#                         ans += 1
#                 elif k == n-1 and l == n-1:
#                     if arr2[k][l] == arr2[k-1][l]:
#                         ans += 1
#                     elif arr2[k][l] == arr2[k][l-1]:
#                         ans += 1

#                 if arr[k][l] == 0:
#                     ans = 0

#         Max = max(ans, Max)

# print(Max)