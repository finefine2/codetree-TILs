a, b, c, d = map(int, input().split())

if c <= b <= d:
    print("intersecting")
    # print("1")
elif c <= a <= d:
    print("intersecting")
    # print("2")
elif a <= c <= b and a <= b <= d:
    print("intersecting")
    # print("3")
elif c <= a <= d and a <= d <= b:
    print("intersecting")
    # print("4")
else:
    print("nonintersecting")