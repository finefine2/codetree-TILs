n = int(input())

arr = []
for i in range(n):
    a = int(input())
    arr.append(a)

s1, e1 = map(int, input().split())
s2, e2 = map(int, input().split())



a = arr[:s1-1] + arr[e1:]

b = a[:s2-1] + a[e2:]

print(len(b))
for k in b:
    print(k)