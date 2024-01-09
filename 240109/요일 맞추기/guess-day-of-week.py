arr = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

a, b, c, d = map(int, input().split())

check = False
ans = 0
if a == c:
   ans = (d - b)
elif a > c:
    for i in range(c, a):
        b += arr[i]
    # b += 1
    ans = b - d
    check = True
else:
    for i in range(a, c):
        d += arr[i]
    # d += 1
    ans = d - b

day = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
day2 = ['Mon', 'Sun', 'Sat', 'Fri', 'Thu', 'Wed', 'Tue']
# print(ans)
if not check:
    print(day[ans % 7])
else:
    print(day2[ans % 7])