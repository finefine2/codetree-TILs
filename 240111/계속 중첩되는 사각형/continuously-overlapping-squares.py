n = int(input())

arr = [[0] * 300 for _ in range(300)]

arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

for t in range(n):
    if t % 2 == 0:
        for i in range(arr1[0], arr1[2]):
            for j in range(arr1[1], arr1[3]):
                arr[i+100][j+100] = 1
    else:
        for i in range(arr2[0], arr2[2]):
            for j in range(arr2[1], arr2[3]):
                arr[i+100][j+100] = -1

ans = 0
for i in range(200):
    for j in range(200):
        if arr[i][j] == -1:
            ans += 1

print(ans)