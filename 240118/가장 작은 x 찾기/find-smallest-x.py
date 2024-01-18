n = int(input())

arr = []
for i in range(n):
    a, b = map(int, input().split())
    arr.append((a, b))

ans = 0
for i in range(1, 10001):
    cnt = 0
    for j in range(n):
        if arr[j][0] <= (2 ** (j+1)) * i <= arr[j][1]:
            cnt += 1
    if cnt == n:
        ans = i
        break

print(ans)