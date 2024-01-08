n, m = map(int, input().split())

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def lcd(n, m):
    return (n * m) // gcd(n, m) 

print(lcd(n, m))