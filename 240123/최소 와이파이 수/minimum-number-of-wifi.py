n, m = map(int, input().split())

arr = list(map(int, input().split()))

one = 0
for k in arr:
    if k == 1:
        one += 1
    
r = m * 2 + 1

if one % r == 0:
    print(one // r)
else:
    print(one // r)