n = int(input())

b = []
for i in range(n):
    a = int(input())
    b.append(a)

b_card = set(b)

a = []
for num in range(1, 2 * n + 1):
    if num not in b_set:
        a.append(num)

a.sort()
b.sort()

ans = 0
idx = 0

for a_idx in range(n):
    if idx < n and a[a_idx] > b[idx]:
        ans += 1
        idx += 1

print(ans)