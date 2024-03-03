n = int(input())
arr = list(map(int, input().split()))

MAX = max(arr)
num = [0] * (MAX + 1)

left, right = 0, 0
ans = 0

while right < n:
    if num[arr[right]] < 1:
        num[arr[right]] += 1
        right += 1
        ans = max(ans, right - left)  
    else:
        num[arr[left]] -= 1
        left += 1

print(ans)