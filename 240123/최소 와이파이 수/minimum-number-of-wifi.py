n, m = map(int, input().split())

arr = list(map(int, input().split()))

one = 0

num = 0
i = 0
while True:
    if i >= n:
        break
    
    if arr[i] == 0:
        i += 1
        continue
    
    num += 1
    i += 2*m+1

print(num)