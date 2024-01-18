n = int(input())

arr = []
for i in range(n):
    a, b = map(int, input().split())
    arr.append((a, b))

# x = set()
# y = set()

# for xx, yy in arr:
#     x.add(xx)
#     y.add(yy)

# if len(x) <= 3 or len(y) <= 3:
#     print(1)
# else:
#     print(0)

check = False
for i in range(11):
    for j in range(11):
        for k in range(11):
            for a in range(2):
                for b in range(2):
                    for c in range(2):
                        flag = True
                        for point in arr:
                            if point[a] == i or point[b] == j or point[c] == k:
                                continue
                            flag = False
                        if flag:
                            check = True
            

if check:
    print(1)
else:
    print(0)