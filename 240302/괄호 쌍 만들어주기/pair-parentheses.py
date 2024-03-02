st = input()

n = len(st)
arr = [0] * n
arr[n-1] = 0

for i in range(n-2, -1, -1):
    if st[i] == ')' and st[i+1] == ')':
        arr[i] = arr[i+1] + 1
    else:
        arr[i] = arr[i+1]
    
ans = 0
for i in range(n-2):
    if st[i] == '(' and st[i+1] == '(':
        ans += arr[i+2]

print(ans)