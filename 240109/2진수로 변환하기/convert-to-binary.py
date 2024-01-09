n = int(input())

arr = []
while True:
    if n < 2:
        arr.append(n)
        break
    arr.append(n % 2)
    n //= 2

for k in arr[::-1]:
    print(k, end = "")