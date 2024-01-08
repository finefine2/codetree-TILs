n = int(input())

s = 0
def func(n):
    global s
    if n == 0:
        return n
    s += (n % 10) * (n % 10)
    return func(n // 10) + (n % 10) * (n % 10)

k = func(n)
print(s)