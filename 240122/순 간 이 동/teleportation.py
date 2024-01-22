a, b, x, y = map(int, input().split())

ans = 101

ans = min(ans, abs(b - a))
ans = min(ans, abs(a - x) + abs(b - y))
ans = min(ans, abs(a - y) + abs(b - x))

print(ans)