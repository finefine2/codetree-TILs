n = int(input())

cnt = 0
def f(n):
    global cnt
    if n == 1:
        return
    if n % 2 == 0:
        cnt += 1
        f(n//2)
    else:
        cnt += 1
        f(n * 3 + 1)

f(n)
print(cnt)