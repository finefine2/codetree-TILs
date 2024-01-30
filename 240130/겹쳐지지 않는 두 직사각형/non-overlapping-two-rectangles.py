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

def square(x1, y1, x2, y2):
    for i in range(n):
        for j in range(m):
            for k in range(i, n):
                for l in range(j, m):
                    for ii in range(n):
                        for jj in range(m):
                            check[ii][jj] = 0
                    s1 = 0
                    for ii in range(x1, x2+1):
                        for jj in range(y1, y2+1):
                            check[ii][jj] += 1
                            s1 += arr[ii][jj]
                    s2 = 0
                    for ii in range(i, k+1):
                        for jj in range(j, l+1):
                            check[ii][jj] += 1
                            s2 += arr[ii][jj]
                    if check_func():
                        ans.append(s1+s2)

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