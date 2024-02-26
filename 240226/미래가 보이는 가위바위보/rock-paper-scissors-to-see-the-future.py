n = int(input())

arr = []
for i in range(n):
    a = input()
    arr.append(a)

L = [0] * (n+1)
R = [0] * (n+1)

for st in "HSP":
    cnt = 0
    for i in range(n):
        if arr[i] == st:
            cnt += 1
        
        L[i] = max(L[i], cnt)

for st in "HSP":
    cnt = 0
    for i in range(n-1, -1, -1):
        if arr[i] == st:
            cnt += 1

        R[i] = max(R[i], cnt)

ans = 0
for i in range(n-1):
    ans = max(ans, L[i] + R[i+1])

print(ans)