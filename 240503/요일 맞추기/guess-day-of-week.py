m1, d1, m2, d2 = map(int, input().split())

month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

ans = 0
if m1 == m2:
    ans = (d2 - d1)
else:
    for i in range(m1, m2):
        ans += month[i]
    ans = (d2 - d1)

print(day[ans % 7])