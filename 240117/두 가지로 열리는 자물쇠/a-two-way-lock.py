n = int(input())
a1, b1, c1 = map(int, input().split())
a2, b2, c2 = map(int, input().split())

def diff(num):
    if abs(num) >= n//2 + 1:
        num = n - abs(num)
    return abs(num)


ans = 0
for i in range(1,n+1):
    for j in range(1,n+1):
        for k in range(1,n+1):
            if (diff(i - a1) <= 2 and diff(j - b1) <= 2 and diff(k - c1) <= 2) or (diff(i - a2) <= 2 and diff(j - b2) <= 2 and diff(k - c2) <= 2):
                ans += 1

print(ans)