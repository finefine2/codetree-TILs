n = int(input())

arr = list(map(int, input().split()))
arr2 = []
for i in range(n):
    arr2.append(arr[i])
    arr2.sort()
    if i % 2 == 0:
        print(arr2[len(arr2)//2], end = " ")