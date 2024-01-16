st = input()

ans = 0
for i in range(len(st)-1):
    if st[i] == '(' and st[i+1] == '(':
        for j in range(i+2, len(st)-1):
            if st[j] == ')' and st[j+1] == ')':
                ans += 1

print(ans)