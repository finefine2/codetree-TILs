a, b = map(int, input().split())

def check(n):
    return '3' in str(n) or '6' in str(n) or '9' in str(n)

def three(n):
    return n % 3 == 0

cnt = 0
for i in range(a, b+1):
    if check(i) or three(i):
        cnt += 1
print(cnt)