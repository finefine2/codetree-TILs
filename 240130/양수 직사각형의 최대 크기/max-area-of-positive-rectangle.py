n, m = map(int, input().split())

arr = []
for i in range(n):
    st = list(map(int, input().split()))
    arr.append(st)

ans = [-1]
check = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if arr[i][j] >= 0:
            check[i][j] = 1

for i in range(n):
    for j in range(m):
        for k in range(i, n):
            for l in range(j, m):
                s = 0
                flag = False
                for ii in range(i, k+1):
                    for jj in range(j, l+1):
                        if check[ii][jj] != 1:
                            flag = True
                        s += arr[ii][jj]
                
                if not flag:
                    ans.append((k-i+1)*(l-j+1))

print(max(ans))