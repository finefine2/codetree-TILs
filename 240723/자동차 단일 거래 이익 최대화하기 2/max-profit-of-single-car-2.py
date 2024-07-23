n = int(input())
arr = list(map(int, input().split()))

Max = 0
Min = arr[0]
for i in range(n):
    cost = arr[i] - Min

    if cost > Max:
        Max = cost
    
    if Min > arr[i]:
        Min = arr[i]


print(Max)