n, c, g, h = map(int, input().split())

def tmp(num, a, b):
    if num < a:
        return c
    elif a <= num <= b:
        return g
    else:
        return h

Max = -1
arr = []
for i in range(n):
    a, b = map(int, input().split())
    arr.append((a, b))

for i in range(1000):
    s = 0
    for j in range(n):
        s += tmp(i, arr[j][0], arr[j][1])
    Max = max(Max, s)

print(Max)