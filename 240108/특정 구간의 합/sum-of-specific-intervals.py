n, m = map(int, input().split())
arr = list(map(int, input().split()))

def func(a1, a2):
    global arr
    s = 0
    for i in range(a1-1, a2):
        s += arr[i]
    return s

for _ in range(m):
    a, b = map(int, input().split())
    print(func(a, b))