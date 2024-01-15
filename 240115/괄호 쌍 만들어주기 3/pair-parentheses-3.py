st = input()

ans = 0
for i in range(len(st)):
    if st[i] == '(':
        for j in range(i, len(st)):
            if st[j] == ')':
                ans += 1


print(ans)