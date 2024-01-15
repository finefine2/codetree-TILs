import sys

n = int(input())

arr = list(map(int, input().split()))

Min = sys.maxsize
for i in range(n):

    dist = 0
    for j in range(n):
        dist += abs(i - j) * arr[j]
    if Min > dist:
        Min = dist

print(Min)