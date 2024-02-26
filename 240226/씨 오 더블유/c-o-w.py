n = int(input())

st = input()

L = [0] * (n+1)
R = [0] * (n+1)

if st[0] == 'C':
    L[0] = 1

for i in range(1, n):
    if st[i] == 'C':
        L[i] = L[i-1] + 1
    else:
        L[i] = L[i-1] + 0

if st[-1] == 'W':
    R[n-1] = 1

for i in range(n-2, -1, -1):
    if st[i] == 'W':
        R[i] = R[i+1] + 1
    else:
        R[i] = R[i+1] + 0

ans = 0
for i in range(1, n-1):
    if st[i] == 'O':
        ans += L[i-1] * R[i+1]

print(ans)