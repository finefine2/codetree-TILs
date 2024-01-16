import sys

n, h, t = map(int, input().split())

arr = list(map(int, input().split()))

arr.sort()

Min = sys.maxsize
for i in range(n-t+1):
    ans = 0
    for j in range(t):
        ans += abs(h - arr[i+j])
    
    if ans < Min:
        Min = ans

print(Min)