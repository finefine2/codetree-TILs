n = int(input())

arr = list(map(int, input().split()))

arr.sort()

arr2 = []
for i in range(len(arr)):
    arr2.append(arr[i] + arr[len(arr)-i-1])

arr2.sort(reverse=True)
print(arr2[0])