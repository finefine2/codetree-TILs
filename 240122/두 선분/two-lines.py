a, b, c, d = map(int, input().split())

if a < b and b < c and c < d:
    print("nonintersecting")
elif c < d and d < a and a < b:
    print("nonintersecting")
else:
    print("intersecting")




# a b 

# c d

# a b c d
# c d a b