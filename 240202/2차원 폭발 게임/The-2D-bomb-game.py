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

new_arr = [[0] * n for _ in range(n)]
def rotate():
    global arr
    for i in range(n):
        for j in range(n):
            new_arr[i][j] = 0
    
    for i in range(n):
        for j in range(n):
            new_arr[i][j] = arr[j][n - 1 - i]
    
    for i in range(n):
        for j in range(n):
            arr[i][j] = new_arr[i][j]

def explode():
    check = False
    for j in range(n):
        cnt = 1
        for i in range(1, n):
            if arr[i][j] == arr[i-1][j] and arr[i][j] != 0:
                cnt += 1
            else:
                if cnt >= m:
                    for k in range(i - cnt, i):
                        arr[k][j] = 0
                    check = True
                cnt = 1
        
        # 마지막 용
        if cnt >= m:
            for k in range(n - cnt, n):
                arr[k][j] = 0
            check = True

    return check


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