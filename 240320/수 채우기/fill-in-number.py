n = int(input())

ans = 0

ans += (n // 5)
n -= (n // 5) * 5

if n % 2 != 0:
    print(-1)
else:
    ans += (n // 2)
    print(ans)