arr = []

n = int(input())

num = 0
cnt = 0
Max = -1
for i in range(n):
    a = int(input())
    if i == 0:
        arr.append(a)
        num = a
        cnt = 1
    else:
        arr.append(a)
        if num == a:
            cnt += 1
            if Max < cnt:
                Max = cnt
        else:
            num = a
            cnt = 1

if n == 1:
    print(1)
else:
    print(Max)