n, m = map(int, input().split())

arr = list(map(int, input().split()))

def func(m):
    if m % 2 != 0:
        m -= 1
    else:
        m //= 2
    return m

s = 0
while m != 1:
    s += arr[m-1]
    m = func(m)
    
s += arr[0]


print(s)