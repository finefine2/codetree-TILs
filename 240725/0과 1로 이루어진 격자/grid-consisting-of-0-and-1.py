n = int(input())

arr = []
for i in range(n):
    tmp = input()
    arr.append([int(k) for k in tmp])

def flip(arr, x, y, n):
    for i in range(x+1):
        for j in range(y+1):
            arr[i][j] = 1 - arr[i][j]

ans = 0
for i in range(n-1, -1, -1):
    for j in range(n-1, -1, -1):
        if arr[i][j] == 1:
            flip(arr, i, j, n)
            ans += 1
            
print(ans)