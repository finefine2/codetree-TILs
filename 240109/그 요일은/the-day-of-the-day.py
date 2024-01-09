arr = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

a, b, c, d = map(int, input().split())
st = input()
idx = 0
for i in range(len(day)):
    if st == day[i]:
        idx = i

if b > d:
    c -= 1
    d += arr[c]

ans = 0
for i in range(a, c):
    ans += arr[i]

ans += d - b

# 5
num = (ans // 7)
if ans % 7 >= idx+1:
    num += 1

print(num)