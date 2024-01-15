n, m = map(int, input().split())

dx = [0,0,1,-1]
dy = [1,-1,0,0]

arr = [[0] * (n+5) for _ in range(n+5)]

for i in range(m):
    a, b = map(int, input().split())
    arr[a][b] = 1

    cnt = 0
    if arr[a-1][b] == 1:
        cnt += 1
    if arr[a][b-1] == 1:
        cnt += 1
    if arr[a+1][b] == 1:
        cnt += 1
    if arr[a][b+1] == 1:
        cnt += 1
    
    if cnt == 3:
        print(1)
    else:
        print(0)