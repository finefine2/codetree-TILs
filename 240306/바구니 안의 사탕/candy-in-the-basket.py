# n, k = map(int, input().split())

# arr = [0] * 1000001
# for i in range(n):
#     candy, basket = map(int, input().split())
#     # arr.append((candy, basket))
#     arr[basket] = candy

# s = [0] * 1000001
# s[0] = arr[0]
# for i in range(n-1):
#     s[i+1] = s[i] + arr[i]

# left = 0
# right = 2*k
# ans = 0

# while True:
#     if right == n-1:
#         break
    
#     c = s[right] - s[left]
#     ans = max(ans, c)

#     left += 1
#     right += 1

# print(ans)


n, k = map(int, input().split())

arr = [0] * 1000001
for _ in range(n):
    candy, basket = map(int, input().split())
    arr[basket] += candy  

s = [0] * 1000001
for i in range(1, 1000001):
    s[i] = s[i-1] + arr[i]

ans = 0

for i in range(1000001):
    left = max(0, i-k)  # 범위 밖으로 나가지 않게
    right = min(1000000, i+k)  # 범위 밖으로 나가지 않게
    if left == 0:
        ans = max(ans, s[right])
    else:
        ans = max(ans, s[right] - s[left-1])

print(ans)