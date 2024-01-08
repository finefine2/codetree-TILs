n = int(input())

cnt = 0
def f(n):
    global cnt
    if n == 1:
        return
    if n % 2 == 0:
        # n //= 2
        cnt += 1
        f(n//2)
    else:
        # n //= 3
        cnt += 1
        f(n//3)

f(n)
print(cnt)