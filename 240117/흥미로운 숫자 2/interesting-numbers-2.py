x, y = map(int, input().split())


def inter(num):
    s = set()
    while num:
        s.add(num % 10)
        num //= 10
    
    if len(s) == 2:
        return True
    else:
        return False

ans = 0
for i in range(x, y+1):
    if inter(i):
        ans += 1

print(ans)