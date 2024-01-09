n = int(input())

arr = [0] * (n+301)
for _ in range(n):
    a, b = map(int, input().split())
    for i in range(a+100, b+100):
        arr[i] += 1
    if a+1 == b:
        arr[a] += 1

print(max(arr))