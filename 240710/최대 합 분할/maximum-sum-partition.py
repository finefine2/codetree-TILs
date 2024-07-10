n = int(input())
arr = list(map(int, input().split()))

s = sum(arr)
num = s //2
dp = [0] * (num + 1)
dp[0] = 1

for k in arr:
    for j in range(num, k-1, -1):
        if dp[j - k]:
            dp[j] = True

for i in range(num, -1, -1):
    if dp[i]:
        print(i)
        exit(0)

print(0)