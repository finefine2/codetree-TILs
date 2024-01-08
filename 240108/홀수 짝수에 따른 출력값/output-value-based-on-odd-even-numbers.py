n = int(input())

s = 0
def f(n):
    global s
    if n == 1:
        s += 1
        return
    if n == 2:
        s += 2
        return
    if n % 2 != 0:
        s += n
        f(n-2)
    else:
        s += n
        f(n-2)

f(n)
print(s)