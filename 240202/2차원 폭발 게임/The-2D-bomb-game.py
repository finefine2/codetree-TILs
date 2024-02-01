n, m, k = map(int, input().split())

arr = []
for i in range(n):
    tmp = list(map(int, input().split()))
    arr.append(tmp)

def gravity():
    for j in range(n):
        col = []
        for i in range(n):
            if arr[i][j] != 0:
                col.append(arr[i][j])
                arr[i][j] = 0
        for i in range(n - len(col), n):
            arr[i][j] = col[i - (n - len(col))]


def rotate():
    global arr
    new_arr = [[0] * n for _ in range(n)]

    
    for i in range(n):
        for j in range(n):
            new_arr[i][j] = arr[j][n - 1 - i]
    
    for i in range(n):
        for j in range(n):
            arr[i][j] = new_arr[i][j]

# def explode():
#     check = False
#     for j in range(n):
#         cnt = 1
#         for i in range(1, n):
#             if arr[i][j] == arr[i-1][j] and arr[i][j] != 0:
#                 cnt += 1
#             else:
#                 if cnt >= m:
#                     for k in range(i - cnt, i):
#                         arr[k][j] = 0
#                     check = True
#                 cnt = 1
        
#         # 마지막 용
#         if cnt >= m:
#             for k in range(n - cnt, n):
#                 arr[k][j] = 0
#             check = True

#     return check

def explode():
    exploded = False
    mark = [[False] * n for _ in range(n)]  # 폭발할 위치를 표시하기 위한 배열

    # 각 열별로 연속된 숫자들이 m개 이상 있는지 확인
    for j in range(n):
        i = 0
        while i < n:
            if arr[i][j] == 0:
                i += 1
                continue
            start = i
            while i < n and arr[start][j] == arr[i][j]:
                i += 1
            if i - start >= m:
                for k in range(start, i):
                    mark[k][j] = True
                exploded = True
    
    # 폭발할 위치의 숫자를 0으로 변경
    for i in range(n):
        for j in range(n):
            if mark[i][j]:
                arr[i][j] = 0

    return exploded


for _ in range(k):
    while explode():
        gravity()
    rotate()


ans = 0
for i in range(n):
    for j in range(n):
        if arr[i][j] != 0:
            ans += 1

print(ans)