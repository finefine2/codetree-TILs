n = int(input())

arr = list(map(int, input().split()))

flag = False

if sum(arr) % 4:
    flag = True
    print(0)
    quit()

s = sum(arr) // 4

L = [0] * (n+1)
R = [0] * (n+1)

num = arr[0]
cnt = 0
if num == s:
    cnt = 1

for i in range(1, n):
    num += arr[i]

    if num == 2 * s:
        L[i] = cnt
    
    if num == s:
        cnt += 1

R[n-1] = 0
num = arr[n-1]
cnt = 0
if num == s:
    cnt = 1

for i in range(n-2, -1, -1):
    num += arr[i]

    if num == 2 * s:
        R[i] = cnt
    
    if num == s:
        cnt += 1

ans = 0

for i in range(1, n-1):
    ans += L[i] * R[i + 1]

print(ans)