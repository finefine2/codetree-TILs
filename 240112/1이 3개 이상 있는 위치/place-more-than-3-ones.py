n = int(input())

arr = []
for i in range(n):
    tmp = list(map(int, input().split()))
    arr.append(tmp)

dx = [0,1,0,-1]
dy = [1,0,-1,0]

def isin(x, y):
    return 0<=x<n and 0<=y<n


ans = 0
for i in range(n):
    for j in range(n):
        cnt = 0
        for dxs, dys in zip(dx, dy):
            nx, ny = i + dxs, j + dys 
            if  isin(nx, ny) and arr[nx][ny] == 1:
                cnt += 1
        if cnt >= 3:
            ans += 1
        
print(ans)