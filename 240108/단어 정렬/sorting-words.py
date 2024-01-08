n = int(input())

arr = []
for _ in range(n):
    a = input()
    arr.append(a)

arr.sort()
for k in arr:
    print(k)