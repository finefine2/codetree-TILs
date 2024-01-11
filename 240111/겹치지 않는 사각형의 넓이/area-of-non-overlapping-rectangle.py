arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
arr3 = list(map(int, input().split()))

n = 3000
arr = [[0] * n for _ in range(n)]

for i in range(arr1[0]+1000, arr1[2]+1000):
    for j in range(arr1[1]+1000, arr1[3]+1000):
        arr[i][j] = 1

for i in range(arr2[0]+1000, arr2[2]+1000):
    for j in range(arr2[1]+1000, arr2[3]+1000):
        arr[i][j] = -1

for i in range(arr3[0]+1000, arr3[2]+1000):
    for j in range(arr3[1]+1000, arr3[3]+1000):
        arr[i][j] = 3

ans = 0
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1 or arr[i][j] == -1:
            ans += 1

print(ans)