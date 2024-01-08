a, b = map(int, input().split())

def func(a, b):
    if a >= b:
        a *= 2
        b += 10
    else:
        a += 10
        b *= 2
    return a, b

n, m = func(a, b)

print(n, m)