a, b, c, d = map(int, input().split())

if a < b < c < d: 
    print("nonintersecting")
elif c < d < a < b:
    print("nonintersecting")
else:
    print("intersecting")