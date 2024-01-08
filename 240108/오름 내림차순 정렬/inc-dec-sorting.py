n = int(input())

arr = list(map(int, input().split()))

arr.sort()

for k in arr:
    print(k, end = " ")

print()

arr.sort(reverse=True)
for k in arr:
    print(k, end = " ")