import sys
n = int(input())

arr = []
for i in range(n):
    a, b = map(int, input().split())
    arr.append((a, b))

Min = sys.maxsize
for i in range(101):
    for j in range(101):
        a = 0
        b = 0
        c = 0
        d = 0
        for k in range(n):
            if arr[k][0] >= i and arr[k][1] >= j:
                a += 1
            elif arr[k][0] < i and arr[k][1] >= j:
                b += 1
            elif arr[k][0] >= i and arr[k][1] < j:
                c += 1
            elif arr[k][0] < i and arr[k][1] < j:
                d += 1
        ans = max(a, b, c, d)
        if Min > ans:
            Min = ans
        # Min = min(Min, ans)

print(Min)