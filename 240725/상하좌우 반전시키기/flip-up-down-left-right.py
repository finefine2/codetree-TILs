n = int(input())

arr = []
for i in range(n):
    tmp = list(map(int, input().split()))
    arr.append(tmp)

def flip(arr, x, y, n):
    arr[x][y] = 1 - arr[x][y]

    if x > 0:
        arr[x - 1][y] = 1 - arr[x - 1][y]
    if x < n-1:
        arr[x + 1][y] = 1 - arr[x + 1][y]
    if y > 0:
        arr[x][y - 1] = 1 - arr[x][y - 1]
    if y < n-1:
        arr[x][y + 1] = 1 - arr[x][y + 1]

ans = 0
for i in range(1, n):
    for j in range(n):
        if arr[i-1][j] == 0:
            flip(arr, i, j, n)
            ans += 1
# 위의 행에서부터 차례대로 내려오면서 확인하는 행의 바로 위부분이 0일 경우 flip을 진행한다.

for j in range(n):
    if arr[n - 1][j] == 0:
        ans = -1
# 만약에 위의 과정을 다 거쳤는데 맨 밑의 줄에 9이 있을 경우 안되는 것이다.


print(ans)