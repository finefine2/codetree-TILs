n = int(input())

arr1 = [0] * 200200

idx = 100000
for _ in range(n):
    a, b = map(str, input().split())
    a = int(a)
    if b == 'L':
        for i in range(idx - a + 1, idx+1):
            arr1[i] = 1
        idx -= a - 1
    else:
        for i in range(idx, idx + a):
            arr1[i] = -1
        idx += a - 1
    
black = 0
white = 0
for i in range(200000):
    if arr1[i] == 1:
        white += 1
    elif arr1[i] == -1:
        black += 1

print(white, black)