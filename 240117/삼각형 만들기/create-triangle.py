n = int(input())

arr = []
for i in range(n):
    a, b = map(int, input().split())
    arr.append((a, b))

Max = -1
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if i == j or j == k or k == i:
                continue
            if arr[i][0] == arr[j][0] and arr[j][1] == arr[k][1]:
                Max = max(Max, abs(arr[i][1] - arr[j][1]) * abs(arr[j][0] - arr[k][0]))
            elif arr[i][1] == arr[j][1] and arr[j][0] == arr[k][0]:
                Max = max(Max, abs(arr[i][0] - arr[j][0]) * abs(arr[j][1] - arr[k][1]))
            elif arr[i][1] == arr[k][1] and arr[j][0] == arr[k][0]:
                Max = max(Max, abs(arr[i][0] - arr[j][0]) * abs(arr[j][1] - arr[k][1]))

print(Max)