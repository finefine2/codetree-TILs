# a, b, c, d = map(int, input().split())

# if b >= d:
#     d += 60
#     c -= 1

# print(d - b + (c - a) * 60)

a, b, c, d = map(int, input().split())

print(c * 60 + d - (a * 60 + b))