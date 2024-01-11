n, m, k = map(int, input().split())

arr = [0] * (n+1)
arr2 = []
ans = 0
for i in range(m):
    a = int(input())

    arr[a] += 1
    if arr[a] >= k:
        ans = a
        break

print(ans)