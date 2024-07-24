n = int(input())

arr = []
for i in range(n):
    a, b = map(int, input().split())
    arr.append((a, b))

ans = 0
arr.sort(key=lambda x : -x[1])


end = 100000
for k in arr:
    if k[1] <= end:
        end = k[0]
        ans += 1

print(n - ans)