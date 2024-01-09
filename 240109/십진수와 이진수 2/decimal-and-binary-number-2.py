n = input()

num = 0
for k in n:
    num = num * 2 + int(k)

num *= 17

arr = []
while True:
    if num < 2:
        arr.append(num)
        break
    arr.append(num % 2)
    num //= 2

for k in arr[::-1]:
    print(k, end = "")