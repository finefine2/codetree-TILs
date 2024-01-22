n, k = map(int, input().split())

arr = []
for i in range(n):
    a = int(input())
    arr.append(a)

bomb = [0] * 1000001

for i in range(n-k+1):
    for j in range(i, i+k):
        if arr[j] == 0:
            bomb[arr[j]] = 1
        else:
            bomb[arr[j]] += 1

Max = 0
Maxidx = 0

for i in range(len(bomb)):
    if bomb[i] > Max:
        Max = bomb[i]
        Maxidx = i

print(Maxidx)