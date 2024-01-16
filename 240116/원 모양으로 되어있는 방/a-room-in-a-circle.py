import sys

n = int(input())

arr = []
for i in range(n):
    a = int(input())
    arr.append(a)

Min = sys.maxsize
for i in range(n):
    ans = 0

    for j in range(n):
        if j == i:
            continue
        ans += ((n - i + j) % n) * arr[j]
        
    
    if ans < Min:
        Min = ans

print(Min)