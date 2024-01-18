n, k = map(int, input().split())

arr = []
for i in range(n):
    a = int(input())
    arr.append(a)

arr.sort()

ans = -1
for i in range(n):
    for j in range(n):
        if i + j < n:
            if arr[i+j] - arr[i] <= k:
                ans = max(ans, j)

print(ans + 1)