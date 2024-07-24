n = int(input())

st = input()
target = input()

arr = []
for i in range(n):
    if st[i] != target[i]:
        arr.append(1)
    else:
        arr.append(0)

ans = 0
tmp = -1
for k in arr:
    if k == 1 and tmp != 1:
        ans += 1
        tmp = 1
    elif k == 0 and tmp != 0:
        tmp = 0

print(ans)