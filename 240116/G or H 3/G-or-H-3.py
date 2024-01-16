n, k = map(int, input().split())

arr = [0] * 10010
for _ in range(n):
    a, b = map(str, input().split())
    if b == 'H':
        arr[int(a)] = 2
    else:
        arr[int(a)] = 1

Max = -1
for i in range(100):
    ans = 0
    for j in range(i, i+k+1):
        ans += arr[j]
    if Max < ans:
        Max = ans
    
print(Max)