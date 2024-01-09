a, b, c, d = map(int, input().split())

if b >= d:
    d += 60
    c -= 1

print(d - b + (c - a) * 60)