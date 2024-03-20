n = int(input())

arr = list(map(int, input().split()))

Max = 0
Min = arr[0]

for i in range(n):
    gain = arr[i] - Min

    if gain > Max:
        Max = gain
    
    if Min > arr[i]:
        Min = arr[i]

print(Max)