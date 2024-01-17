n, k = map(int, input().split())

arr = []
for i in range(n):
    a = int(input())
    arr.append(a)

Max = -1
for i in range(n):
    for j in range(i, n):
        if i == j:
            continue
        if arr[i] == arr[j] and abs(j - i) <= k:
            Max = max(Max, arr[i])

print(Max)