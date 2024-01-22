a, b, c, d = map(int, input().split())

if b >= c and b <= d:
    print("intersecting")
elif c <= a <= d:
    print("intersecting")
elif a <= b and c <= d:
    print("intersecting")
elif b <= a and d <= c:
    print("intersecting")
else:
    print("nonintersecting")