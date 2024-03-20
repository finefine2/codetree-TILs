n = int(input())

arr = list(map(int, input().split()))

arr.sort()

ans = 0
while len(arr) > 1:
    num = 0
    ans += arr[0]
    num += arr[0]
    arr.pop(0)

    ans += arr[0]
    num += arr[0]
    arr.pop(0)

    arr.append(num)
    arr.sort()
    # print(ans)

print(ans)