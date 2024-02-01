a, b, c = map(int, input().split())


ans = 0
if a + 1 == b and b + 1 == c:
    ans = 0
else:
    ans = max(c - b - 1, b - a - 1)

print(ans)