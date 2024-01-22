a, b, c, d = map(int, input().split())

if b >= c and b <= d:
    print("intersecting")
elif c <= a <= d:
    print("intersecting")
else:
    print("nonintersecting")