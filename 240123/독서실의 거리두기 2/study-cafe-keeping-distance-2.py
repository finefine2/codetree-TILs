n = int(input())

st = input()

arr = []
idx = 0
for i in range(len(st)):
    if st[i] == '1':
        arr.append(i)
        idx = i


dist = []
for i in range(len(arr)-1):
    dist.append(arr[i+1] - arr[i])

dist.sort()

check = False
if dist[-1] // 2 < len(st) - 1 - idx:
    dist.append(len(st) - 1 - idx)
    check = True

first = st.find("1")
if dist[-1] // 2 < first:
    dist.append(first)
    check = True

dist.sort()

if not check:
    dist[-1] //= 2

# if dist[-1] % 2 == 0:
#     dist[-1] = dist[-1] // 2 + 1
# else:
#     dist[-1] //= 2

# for k in dist:
#     print(k, end = " ")



print(min(dist))

# print()
# print(st.find("1"))