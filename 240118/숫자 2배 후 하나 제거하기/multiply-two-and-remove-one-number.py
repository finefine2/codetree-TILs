import sys
n = int(input())

arr = list(map(int, input().split()))

Min = sys.maxsize
for i in range(n):
    arr[i] *= 2

    for j in range(n):
        s = 0
        arr2 = []
        for k in range(n):
            if j != k:
                arr2.append(arr[k])

        for k in range(n-2):
            s += abs(arr2[k+1] - arr2[k])
        
        Min = min(s, Min)

    arr[i] //= 2

print(Min)