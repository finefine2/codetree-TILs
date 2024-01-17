n, b = map(int, input().split())


arr = []
for i in range(n):
    p, s = map(int, input().split())
    arr.append((p, s))

arr.sort(lambda x : 0.5 * x[0] + x[1])

i = 0
num = 0
s = 0
while True:
    s += arr[i][0] + arr[i][1]
    
    if s > b:
        if s - (arr[i][0] * 0.5):
            num += 1
            break
        else:
            break
    i += 1
    num += 1

print(num)