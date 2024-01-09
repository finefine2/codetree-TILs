a, b, c = map(int, input().split())

ans = 0
check = False
if a < 11 or (a == 11 and b < 11) or (a == 11 and b == 11 and c < 11):
    check = True
elif b < 11:
    b += 24
    a -= 1
elif c < 11:
    c += 60
    b -= 1

if check:
    print(-1)
else:
    print((a - 11) * 1440 + (b - 11) * 60 + (c - 11))