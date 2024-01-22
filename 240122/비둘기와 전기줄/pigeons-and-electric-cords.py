n = int(input())

check = [5] * 101
arr = []
for i in range(n):
    a, b = map(int, input().split())
    arr.append((a, b))

ans = 0
for k in arr:
    if check[k[0]] == 5:
        check[k[0]] = k[1]
    else:
        if check[k[0]] != k[1]:
            ans += 1
            check[k[0]] = k[1]

print(ans)