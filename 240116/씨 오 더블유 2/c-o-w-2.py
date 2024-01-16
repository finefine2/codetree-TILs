n = int(input())

st = input()

ans = 0

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if st[i] == 'C' and st[j] == 'O' and st[k] == 'W':
                ans += 1

print(ans)