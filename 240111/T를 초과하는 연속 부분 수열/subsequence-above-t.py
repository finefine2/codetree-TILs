n, t = map(int, input().split())

arr = list(map(int, input().split()))


num = 0
Max = -1
cnt = 0
for i in range(len(arr)):
    if i == 0:
        if arr[i] > t:
            num = arr[i]
            cnt = 1
        else:
            num = arr[i]
    else:
        if arr[i] > t:
            num = arr[i]
            cnt += 1
            if Max < cnt:
                Max = cnt
        else:
            cnt = 0
            num = arr[i]

if n == 1:
    print(1)
else:
    print(Max)