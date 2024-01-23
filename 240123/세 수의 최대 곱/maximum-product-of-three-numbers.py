n = int(input())

arr = list(map(int, input().split()))

arr.sort()

plus = 0
minus = 0
zero = 0
for k in arr:
    if k > 0:
        plus += 1
    elif k == 0:
        zero += 1
    else:
        minus += 1

ans = 0
if max(arr) == 0:
    ans = 0
elif minus == 0:
    ans = arr[-1] * arr[-2] * arr[-3]
elif plus == 0:
    ans = arr[-1] * arr[-2] * arr[-3]
elif plus == 1:
    ans = arr[0] * arr[1] * arr[-1]
elif n == 3:
    ans = arr[0] * arr[1] * arr[2]
else:
    ans = max(arr[0] * arr[1] * arr[-1], arr[-1] * arr[-2] * arr[-3])

print(ans)

# 3개
# 양양양 -> 제일 크게
# 양음음 -> 제일 크게
# 음음음 -> 제일 작게
# 양양음 -> 제일 작게