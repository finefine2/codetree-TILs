n = int(input())

arr = list(map(int, input().split()))

ans = 0
for k in range(100):
    cnt = 0

    for i in range(n):
        for j in range(i+1, n):
            if (arr[i] + arr[j]) == 2 * k:
                cnt += 1
\
    ans = max(ans, cnt)

print(ans)