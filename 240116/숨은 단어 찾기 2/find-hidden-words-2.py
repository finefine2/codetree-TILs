n, m = map(int, input().split())

arr = []
for i in range(n):
    a = input()
    arr.append(a)

ans = 0
for i in range(n-2):
    for j in range(m):
        if arr[i][j] == 'L' and arr[i+1][j] == 'E' and arr[i+2][j] == 'E':
            ans += 1
        elif arr[i][j] == 'E' and arr[i+1][j] == 'E' and arr[i+2][j] == 'L':
            ans += 1

for i in range(n):
    for j in range(m-2):
        if arr[i][j] == 'L' and arr[i][j+1] == 'E' and arr[i][j+2] == 'E':
            ans += 1
        elif arr[i][j] == 'E' and arr[i][j+1] == 'E' and arr[i][j+2] == 'L':
            ans += 1

for i in range(n-2):
    for j in range(m-2):
        if arr[i][j] == 'L' and arr[i+1][j+1] == 'E' and arr[i+2][j+2] == 'E':
            ans += 1
        elif arr[i][j] == 'E' and arr[i+1][j+1] == 'E' and arr[i+2][j+2] == 'L':
            ans += 1

for i in range(n-2):
    for j in range(2, m):
        if arr[i][j] == 'L' and arr[i+1][j-1] == 'E' and arr[i+2][j-2] == 'E':
            ans += 1
        elif arr[i][j] == 'E' and arr[i+1][j-1] == 'E' and arr[i+2][j-2] == 'L':
            ans += 1

print(ans)