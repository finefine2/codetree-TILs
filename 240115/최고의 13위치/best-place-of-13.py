n = int(input())

arr = []
for i in range(n):
    tmp = list(map(int, input().split()))
    arr.append(tmp)

ans = 0
for i in range(n):
    for j in range(n-2):
        if arr[i][j] == 1 and arr[i][j+1] == 1 and arr[i][j+2] == 1:
            ans = 3
        elif (arr[i][j] == 1 and arr[i][j+1] == 1) or (arr[i][j] == 1 and arr[i][j+2] == 1) or (arr[i][j+1] == 1 and arr[i][j+2] == 1):
            if ans < 2:
                ans = 2
        elif arr[i][j] == 1:
            if ans < 1:
                ans = 1

print(ans)