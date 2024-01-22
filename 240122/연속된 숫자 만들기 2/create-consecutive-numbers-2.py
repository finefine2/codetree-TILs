arr = list(map(int, input().split()))
arr.sort()

ans = 0

if arr[0] + 1 == arr[1] and arr[1] + 1 == arr[2]:
    ans = 0
elif arr[0] + 2 == arr[1] and arr[1] + 2 == arr[2]:
    ans = 1
else:
    ans = 2
# 어떠한 경우든 2번 안에 끝난다..

print(ans)