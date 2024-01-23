n = int(input())

st = input()

arr = []
for i in range(len(st)):
    if st[i] == '1':
        arr.append(i)

dist = []
for i in range(len(arr)-1):
    dist.append(arr[i+1] - arr[i])

dist.sort()
dist[-1] //= 2

print(min(dist))