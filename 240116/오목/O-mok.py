arr = []
for i in range(19):
    tmp = list(map(int, input().split()))
    arr.append(tmp)

ans = 0
x, y = 0,0
for i in range(15):
    for j in range(19):
        if arr[i][j] == 1 and arr[i+1][j] == 1 and arr[i+2][j] == 1 and arr[i+3][j] == 1 and arr[i+4][j] == 1:
            ans = 1
            x = i+2
            y = j
        elif arr[i][j] == 2 and arr[i+1][j] == 2 and arr[i+2][j] == 2 and arr[i+3][j] == 2 and arr[i+4][j] == 2:
            ans = 2
            x = i+2
            y = j

for i in range(19):
    for j in range(15):
        if arr[i][j] == 1 and arr[i][j+1] == 1 and arr[i][j+2] == 1 and arr[i][j+3] == 1 and arr[i][j+4] == 1:
            ans = 1
            x = i
            y = j+2
        if arr[i][j] == 2 and arr[i][j+1] == 2 and arr[i][j+2] == 2 and arr[i][j+3] == 2 and arr[i][j+4] == 2:
            ans = 2
            x = i
            y = j+2

for i in range(15):
    for j in range(15):
        if arr[i][j] == 1 and arr[i+1][j+1] == 1 and arr[i+2][j+2] == 1 and arr[i+3][j+3] == 1 and arr[i+4][j+4] == 1:
            ans = 1
            x = i + 2
            y = j+2
        if arr[i][j] == 2 and arr[i+1][j+1] == 2 and arr[i+2][j+2] == 2 and arr[i+3][j+3] == 2 and arr[i+4][j+4] == 2:
            ans = 2
            x = i + 2
            y = j+2

for i in range(15):
    for j in range(4, 19):
        if arr[i][j] == 1 and arr[i+1][j-1] == 1 and arr[i+2][j-2] == 1 and arr[i+3][j-3] == 1 and arr[i+4][j-4] == 1:
            ans = 1
            x = i + 2
            y = j - 2
        if arr[i][j] == 2 and arr[i+1][j-1] == 2 and arr[i+2][j-2] == 2 and arr[i+3][j-3] == 2 and arr[i+4][j-4] == 2:
            ans = 2
            x = i + 2
            y = j - 2

print(ans)
if ans != 0:
    print(x+1, y+1)