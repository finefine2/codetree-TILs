n1, n2 = map(int, input().split())

arr = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

def check(arr, arr2):
    for i in range(len(arr)):
        if arr[i:i+len(arr2)] == arr2:
            return True
    return False

if check(arr, arr2):
    print("Yes")
else:
    print("No")