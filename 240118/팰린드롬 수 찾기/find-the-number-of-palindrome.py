x, y = map(int, input().split())

ans = 0
for a in range(x, y+1):
    a = str(a)
    if a == a[::-1]:
        ans += 1
print(ans)