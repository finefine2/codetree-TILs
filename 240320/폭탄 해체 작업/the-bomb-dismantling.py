n = int(input())

arr = []
for i in range(n):
    a, b = map(int, input().split())
    arr.append((a, b))

arr.sort(key=lambda x : (x[1], -x[0]))

tmp = arr[0][1]
ans = arr[0][0]
for i in range(1, n):
    if tmp != arr[i][1]:
        ans += arr[i][0]
        tmp = arr[i][1]

print(ans)