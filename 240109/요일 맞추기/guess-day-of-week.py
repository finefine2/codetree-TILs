arr = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

a, b, c, d = map(int, input().split())

ans = 0
if a == c:
   ans = (d - b)
elif a > c:
    for i in range(c, a):
        b += arr[i]
    # b += 1
    ans = b - d
else:
    for i in range(a, c):
        d += arr[i]
    # d += 1
    ans = d - b

day = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

# print(ans)
print(day[ans % 7])