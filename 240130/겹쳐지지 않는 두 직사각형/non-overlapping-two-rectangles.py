n, m = map(int, input().split())

arr = []
for i in range(n):
    st = list(map(int, input().split()))
    arr.append(st)

check = [[0] * m for _ in range(n)]
s = [[0] * m for _ in range(n)]
ans = []

# for i in range(n):
#     for j in range(m):
#         for k in range(i+1):
#             for l in range(j+1):
#                 s[i][j] += arr[k][l]

def check_func():
    for i in range(n):
        for j in range(m):
            if check[i][j] >= 2:
                return False
    return True
    # 2개가 넘을 경우 -> 즉 겹칠 경우에는 답이 될 수 없으므로 False

def square(x1, y1, x2, y2):
    for i in range(n):
        for j in range(m):
            for k in range(i, n):
                for l in range(j, m):
                    for ii in range(n):
                        for jj in range(m):
                            check[ii][jj] = 0
                    # 일단 0으로 초기화

                    s1 = 0
                    for ii in range(x1, x2+1):
                        for jj in range(y1, y2+1):
                            check[ii][jj] += 1
                            s1 += arr[ii][jj]
                    # 첫번째 사각형에 더하고 check 늘리기
                    s2 = 0
                    for ii in range(i, k+1):
                        for jj in range(j, l+1):
                            check[ii][jj] += 1
                            s2 += arr[ii][jj]
                    # 두번째 사각형에 더하고 check 늘리기
                    if check_func():
                        ans.append(s1+s2)
                        # check를 확인해서 겹치지 않는다면 ans에 추가한다.

for i in range(n):
    for j in range(m):
        for k in range(i, n):
            for l in range(j, m):
                square(i, j, k, l)

print(max(ans))

# for i in range(n):
#     for j in range(m):
#         print(s[i][j], end = " ")
#     print()