n = int(input())

arr = [0] * (n+201)
for _ in range(n):
    a, b = map(int, input().split())
    for i in range(a+100, b+99):
        arr[i] += 1

print(max(arr))