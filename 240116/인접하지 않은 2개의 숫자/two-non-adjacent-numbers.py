n = int(input())
arr = list(map(int, input().split()))

Max = -1
for i in range(n):
    for j in range(n):
        if abs(i - j) != 1 and i != j:
            if Max < arr[i] + arr[j]:
                Max = arr[i] + arr[j]

print(Max)