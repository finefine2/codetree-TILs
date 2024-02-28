n = int(input())

arr = []
for i in range(n):
    a, b = map(int, input().split())
    arr.append((a, b))

point = []
for i, (a, b) in enumerate(arr):
    point.append((a, 1, i))
    point.append((b, -1, i))

# 빠지는 길이를 여기에 넣어준다.
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
    # set의 첫번째를 target으로 해서 그 경우에 값을 더한다. 
    # 그 값이 없을 경우의 합을 구하는 것
    if cnt == 1:
        target = list(s)[0]
        check[target] += (x - prev)
    
    if v == 1:
        s.add(idx)
    else:
        s.remove(idx)
    # 1일 경우 더해주고 아닐 경우 지운다.

    prev = x
    # prev를 지금의 x로 갱신한다.

import sys
Min = sys.maxsize
for i in range(n):
    Min = min(Min, check[i])
    # 빠지게 되는 길이의 최솟값을 갱신한다.

print(total - Min)