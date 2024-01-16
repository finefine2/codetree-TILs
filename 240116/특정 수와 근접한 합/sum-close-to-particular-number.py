import sys
n, s = map(int, input().split())

arr = list(map(int, input().split()))

Min = sys.maxsize
x, y = 0, 0
for i in range(n):
    for j in range(i+1, n):
        if abs(s - (sum(arr) - arr[i] - arr[j])) < Min:
            Min = abs(s - (sum(arr) - arr[i] - arr[j]))
            

print(Min)