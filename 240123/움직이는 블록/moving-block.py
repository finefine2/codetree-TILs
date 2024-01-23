n = int(input())

arr = []
for i in range(n):
    a = int(input())
    arr.append(a)

s = sum(arr)
av = sum(arr) // n

ans = 0
for k in arr:
    if k < av:
        ans += (av - k)
    # elif k > av:
    #     ans += (k - av)

print(ans)