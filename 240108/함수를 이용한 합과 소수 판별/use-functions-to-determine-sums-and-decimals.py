a, b = map(int, input().split())


def sosu(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def hap(n):
    n = str(n)
    s = 0
    for k in n:
        s += int(k)
    if s % 2 == 0:
        return True

cnt = 0
for i in range(a, b+1):
    if sosu(i) and hap(i):
        cnt += 1
print(cnt)