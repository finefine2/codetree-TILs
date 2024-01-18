n = int(input())

arr = []
for i in range(n):
    a, b = map(int, input().split())
    arr.append((a, b))

x = set()
y = set()

for xx, yy in arr:
    x.add(xx)
    y.add(yy)

if len(x) + len(y) <= 3:
    print(1)
else:
    print(0)

# check = False
# for i in range(11):
#     for j in range(11):
#         for k in range(11):
#             cnt = 0
#             for l in range(len(arr)):
#                 if arr[l][0] == i or arr[l][1] == i or arr[l][0] == j or arr[l][1] == j or arr[l][0] == k or arr[l][1] == k:
#                     cnt += 1
                
#             if cnt == len(arr):
#                 check = True

# if check:
#     print(1)
# else:
#     print(0)