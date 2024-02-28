n = int(input())

arr = []
for i in range(n):
    a, b = map(int, input().split())
    arr.append((a, b))

point = []
for i, (a, b) in enumerate(arr):
    point.append((a, 1, i))
    point.append((b, -1, i))

check = [0] * n
point.sort()
s = set()
prev = -1
total = 0

for x, v, idx in point:
    cnt = len(s)

    # set의 길이가 0이 넘으면 총 길이에 더해준다.
    if cnt > 0:
        total += (x - prev)
    
    # set의 크기가 1개일 경우 
    if cnt == 1:
        target = list(s)[0]
        check[target] += (x - prev)
    
    if v == 1:
        s.add(idx)
    else:
        s.remove(idx)

    prev = x

import sys
Min = sys.maxsize
for i in range(n):
    Min = min(Min, check[i])

print(total - Min)