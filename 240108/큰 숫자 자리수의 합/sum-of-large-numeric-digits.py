a, b, c = map(int, input().split())


s = a*b*c
k = 0
def f(n):
    global k
    if n == 0:
        return
    k += n % 10
    f(n // 10)

f(s)
print(k)