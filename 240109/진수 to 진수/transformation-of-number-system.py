a, b = map(int, input().split())

n = input()

num = 0
for k in n:
    num = num * a + int(k)

arr = []
while True:
    if num < b:
        arr.append(num)
        break
    arr.append(num % b)
    num //= b

for k in arr[::-1]:
    print(k, end = "")