a, b = map(int, input().split())

def change(a, b):
    a, b = b, a
    return a, b

n, m = change(a, b)
print(n, m)