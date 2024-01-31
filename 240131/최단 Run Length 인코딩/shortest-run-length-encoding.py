a = input()


def run(a):
    cnt = 0
    tmp = ""
    ans = ""
    for i in range(len(a)):
        if i == 0:
            cnt = 1
            tmp = a[i]
        elif i == len(a) - 1:
            if tmp == a[i]:
                cnt += 1
                ans += tmp
                ans += str(cnt)
            else:
                ans += tmp
                ans += str(cnt)
                cnt = 1
                ans += a[i]
                ans += str(cnt)
        else:
            if tmp == a[i]:
                cnt += 1
            else:
                ans += tmp
                ans += str(cnt)
                cnt = 1
                tmp = a[i]

    return ans

Min = 100
st = ""
l = len(a)
if l == 1:
    Min = 2
else:
    for i in range(l):
        a = a[-1] + a[:-1]
        b = run(a)
        if len(b) < Min:
            Min = len(b)

print(Min)