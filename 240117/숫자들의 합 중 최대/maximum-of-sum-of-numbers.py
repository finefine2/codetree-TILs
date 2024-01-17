x, y = map(int, input().split())

Max = -1
for k in range(x, y+1):
    s = 0
    while k:
        s += k % 10
        k //= 10
    Max = max(Max, s)

print(Max)