n = int(input())

Max = -1
cnt = 1
num = 0
for i in range(n):
    a = int(input())

    if i == 0:
        num = a
    else:
        if num < a:
            cnt += 1
            num = a
            if Max < cnt:
                Max = cnt
        else:
            cnt = 1
            num = a

if n == 1:
    print(1)
else:
    print(Max)