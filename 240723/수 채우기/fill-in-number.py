n = int(input())

ans = 100001
for i in range(100001):
    rem = n - 5 * i
    if rem >= 0 and rem % 2 == 0:
        ans = min(ans, i + rem // 2)

if ans == 100001:
    print(-1)
else:
    print(ans)