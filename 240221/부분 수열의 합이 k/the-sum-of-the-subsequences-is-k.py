n, k = map(int, input().split())

arr = list(map(int, input().split()))

s = [0] * (n+1)

# s[0] = arr[0]
for i in range(n):
    s[i+1] = s[i] + arr[i]

# for i in range(n):
#     print(s[i], end = " ")
    

ans = 0
for i in range(n):
    for j in range(i+1, n+1):
        if s[j] - s[i] == k:
            ans += 1

print(ans)