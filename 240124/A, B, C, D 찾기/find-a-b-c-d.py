arr = list(map(int, input().split()))

arr.sort()

a = arr[0]
b = arr[1]
cd = arr[-1] - a - b
if a + b != arr[2]:
    c = arr[2]
    d = cd - arr[2]
else:
    c = arr[3]
    d = cd - arr[3]

print(a, b, c, d)

# a b c d
# ab bc cd da ac bd
# abc abd acd bcd 
# abcd