n = int(input())
st = list(input())
target = list(input())

ans = 0
for i in range(len(st)-1, -1, -1):
    if st[i] != target[i]:
        for j in range(0, i+1):
            if st[j] == 'G':
                st[j] = 'H'
            elif st[j] == 'H':
                st[j] = 'G'
        
        ans += 1

print(ans)