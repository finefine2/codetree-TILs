n = int(input())

arr = [0] + list(map(int, input().split()))

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def lcd(a, b):
    return (a * b) // gcd(a, b)

def f(n):
    if n == 1:
        return arr[1]
    return lcd(f(n-1), arr[n])

print(f(n))