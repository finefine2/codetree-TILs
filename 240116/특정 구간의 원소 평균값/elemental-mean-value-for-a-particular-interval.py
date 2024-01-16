n = int(input())

arr = list(map(int, input().split()))

ans = 0
for i in range(n):
    for j in range(i, n):
        s = 0

        for k in range(i, j+1):
            s += arr[k]
        
        av = s / (j - i + 1)
    

        if av in arr:
            ans += 1

print(ans)