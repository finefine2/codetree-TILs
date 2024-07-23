n = int(input())

b = []
for i in range(n):
    num = int(input())
    b.append(num)

b_set = set(b)

a = []
for i in range(1, 2 * n + 1):
    if i not in b_set:
        a.append(i)

a.sort()
b.sort()

ans = 0
b_idx = 0
for a_idx in range(n):
    if b_idx < n and a[a_idx] > b[b_idx]:
        ans += 1
        b_idx += 1

print(ans)