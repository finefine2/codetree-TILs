n, m = map(int, input().split())

arr1 = []
arr2 = []

a, b = 0,0
for i in range(n):
    x, y = map(int, input().split())
    for j in range(y):
        arr1.append(a + x * j)
    a += x * y

for i in range(m):
    x, y = map(int, input().split())
    for j in range(y):
        arr2.append(b + x * j)
    b += x * y

ans = 0
plus = False
for i in range(1, len(arr1)):
    if i == 1:
        if arr1[1] - arr2[1] >= 0:
            plus = True
        else:
            plus = False
    else:
        if arr1[i] - arr2[i] >= 0:
            if not plus:
                plus = True
                ans += 1
        else:
            if plus:
                plus = False
                ans += 1

print(ans)

# for k in arr1:
#     print(k, end = " ")
# print()
# for k in arr2:
#     print(k, end = " ")