# n, k = map(int, input().split())

# arr = list(map(int, input().split()))

# s = [0] * (n+1)

# s[0] = arr[0]
# for i in range(1, n):
#     s[i] = s[i-1] + arr[i]

# ans = 0
# for i in range(1, n - k + 1):
#     num = num - arr[i - 1] + arr[i + k - 1]
#     ans = max(ans, num)

# # for i in range(n-k):
# #     for j in range(i+1, n):
# #         ans = max(ans, s[j] - s[i] + arr[i])

# print(ans)

n, k = map(int, input().split())
arr = list(map(int, input().split()))

s = sum(arr[:k])
ans = s

for i in range(1, n - k + 1):
    s = s - arr[i - 1] + arr[i + k - 1]
    ans = max(ans, s)

print(ans)