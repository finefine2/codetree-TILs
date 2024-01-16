n = int(input())

arr = []
for _ in range(n):
    a = int(input())
    arr.append(a)

def carry(a, b, c):
    k = min(len(str(a)), len(str(b)), len(str(c)))
    for k in range(n):
        x, y = a % 10, b % 10
        z = c % 10
        if x + y + z >= 10:
            return True
        a //= 10
        b //= 10
        c //= 10
    return False

Max = -1
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if not carry(arr[i], arr[j], arr[k]):
                if Max < arr[i] + arr[j] + arr[k]:
                    Max = arr[i] + arr[j] + arr[k]

print(Max)