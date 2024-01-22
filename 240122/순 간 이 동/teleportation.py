a, b, x, y = map(int, input().split())

ans = 101

ans = min(ans, abs(b - a))
# a -> b
ans = min(ans, abs(a - x) + abs(b - y))
# a ->x -> y -> b
ans = min(ans, abs(a - y) + abs(b - x))
# a -> y -> x -> b
# 이 중에서 min을 찾아서 넣어준다.
print(ans)