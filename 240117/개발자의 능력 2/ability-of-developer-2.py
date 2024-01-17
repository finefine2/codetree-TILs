arr = list(map(int, input().split()))

# 합들을 다 비슷하게 하기

arr.sort()

n = len(arr)
arr2 = []
arr2.append(arr[0] + arr[5])
arr2.append(arr[1] + arr[4])
arr2.append(arr[2] + arr[3])

arr2.sort()
print(arr2[2] - arr2[0])