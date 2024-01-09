arr = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


a, b, c, d = map(int, input().split())

if a == c:
    print(d - b + 1)
else:
    for i in range(a, c):
        d += arr[i]
    d += 1
    print(d - b)