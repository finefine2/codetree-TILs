x1, y1, x2, y2 = map(int, input().split())
a1, b1, a2, b2 = map(int, input().split())

if x2 < a1:
    print("nonoverlapping")
elif a2 < x1:
    print("nonoverlapping")
elif b2 < y1:
    print("nonoverlapping")
elif y2 < b1:
    print("nonoverlapping")
else:
    print("overlapping")