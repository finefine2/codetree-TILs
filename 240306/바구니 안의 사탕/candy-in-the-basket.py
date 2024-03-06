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




# def max_candies(n, k, arr):

#     arr.sort(key=lambda x: x[1])

#     left, right = 0, 0
#     current_sum = arr[0][0]  # 현재 윈도우의 사탕 합
#     max_sum = current_sum  # 최대 사탕 합

#     while right < n:
#         # 윈도우의 오른쪽을 확장할 수 있는 경우
#         if right + 1 < n and arr[right + 1][1] - arr[left][1] <= 2 * k:
#             right += 1
#             current_sum += arr[right][0]
#             max_sum = max(max_sum, current_sum)
#         # 윈도우의 왼쪽을 줄여야 하는 경우
#         else:
#             current_sum -= arr[left][0]
#             left += 1
#             if left > right and left < n:  # 왼쪽이 오른쪽을 넘어선 경우
#                 right = left
#                 current_sum = arr[left][0]

#     return max_sum

# n, k = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(n)]

# print(max_candies(n, k, arr))

n, k = map(int, input().split())
candies = []
for _ in range(n):
    candy, basket = map(int, input().split())
    candies.append((basket, candy))

candies.sort()

max_candies = 0
current_candies = 0
left = 0

for right in range(n):
    # 현재 바구니와 비교할 바구니의 위치 차이가 K 이내인 동안 사탕 수를 더함
    while candies[right][0] - candies[left][0] > 2*k:
        current_candies -= candies[left][1]
        left += 1
    current_candies += candies[right][1]
    max_candies = max(max_candies, current_candies)

print(max_candies)