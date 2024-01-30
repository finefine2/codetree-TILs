import copy
n, m, q = map(int, input().split())

arr = []
for i in range(n):
    st = list(map(int, input().split()))
    arr.append(st)


for _ in range(q):
    r1, c1, r2, c2 = map(int, input().split())
    r1 -= 1
    c1 -= 1
    r2 -= 1
    c2 -= 1
    
    tmp = arr[r1][c1]

    # 왼쪽 열 이동
    for i in range(r1, r2):
        arr[i][c1] = arr[i + 1][c1]

    # 아래쪽 행 이동
    for i in range(c1, c2):
        arr[r2][i] = arr[r2][i + 1]

    # 오른쪽 열 이동
    for i in range(r2, r1, -1):
        arr[i][c2] = arr[i - 1][c2]

    # 위쪽 행 이동
    for i in range(c2, c1, -1):
        arr[r1][i] = arr[r1][i - 1]

    # 첫 번째 요소를 마지막에 삽입
    arr[r1][c1 + 1] = tmp

    arr2 = copy.deepcopy(arr)

    for i in range(r1, r2+1):
        for j in range(c1, c2+1):
            cnt = 1
            s = 0
            s += arr2[i][j]
            if i - 1 >= 0:
                s += arr2[i-1][j]
                cnt += 1
            if i + 1 < n:
                s += arr2[i+1][j]
                cnt += 1
            if j - 1 >= 0:
                s += arr2[i][j-1]
                cnt += 1
            if j + 1 < m:
                s += arr2[i][j+1]
                cnt += 1

            arr[i][j] = (s // cnt)
            # print(i, j, s, cnt)
    
for i in range(n):
    for j in range(m):
        print(arr[i][j], end = " ")
    print()

print()

# for i in range(n):
#     for j in range(m):
#         print(arr2[i][j], end = " ")
#     print()