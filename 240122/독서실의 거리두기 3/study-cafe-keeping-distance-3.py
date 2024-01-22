n = int(input())

st = input()

# 양족 끝자리는 항상 사람이 앉아있음

arr = []
for i in range(len(st)):
    if st[i] == '1':
        arr.append(i)

dist = []

for i in range(len(arr) - 1):
    dist.append(arr[i+1] - arr[i])

ans = 0

ans = max(ans, min(min(dist), max(dist) // 2))
# 4 3 4
print(ans)