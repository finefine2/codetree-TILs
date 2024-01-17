n, b = map(int, input().split())

arr = []
for i in range(n):
    a = int(input())
    arr.append(a)

arr.sort()

i = 0
s = 0
cnt = 0
while True:
    s += arr[i]
    
    if s >= b:
        if s - (arr[i] // 2) <= b:
            cnt += 1
            break
        else:
            s -= arr[i]
            break
    
    cnt += 1
    i += 1

print(cnt)