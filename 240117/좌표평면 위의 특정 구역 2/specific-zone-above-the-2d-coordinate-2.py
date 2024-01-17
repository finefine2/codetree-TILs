import sys
n = int(input())

Maxx = 0
Maxy = 0
Max = 0
arr = []
for i in range(n):
    a, b = map(int, input().split())
    arr.append((a, b))

for a, b in arr:
    if a * b > Max:
        Max = a * b
        Maxx = a
        Maxy = b

Maxxx = 0
Maxyy = 0
Minx = sys.maxsize
Miny = sys.maxsize
for a, b in arr:
    if Maxxx < a and a != Maxx:
        Maxxx = a
    if Maxyy < b and b != Maxy:
        Maxyy = b
    if Minx > a:
        Minx = a
    if Miny > b:
        Miny = b


print((Maxxx - Minx) * (Maxyy - Miny))