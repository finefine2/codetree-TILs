import sys

n = int(input())

Min = sys.maxsize
arr = []
for i in range(n):
    a, b = map(int, input().split())
    arr.append((a, b))

for i in range(n):
    for j in range(n):
        if i == j:
            continue
        dist = (arr[i][0] - arr[j][0]) * (arr[i][0] - arr[j][0]) + (arr[i][1] - arr[j][1]) * (arr[i][1] - arr[j][1])
        if dist < Min:
            Min = dist

print(Min)