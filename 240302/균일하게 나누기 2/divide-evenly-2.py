n = int(input())

arr = []
for i in range(n):
    x, y = map(int, input().split())
    arr.append((x, y))

arr.sort()

import sys
ans = sys.maxsize

for k in range(0, 1001, 2):
    area = [0] * 5

    for x, y in arr:
        if y > k:
            area[1] += 1
        else:
            area[4] += 1
    
    # y값을 고정시키고 x를 움직이면서 최소를 찾아준다.
    for i in range(n):
        if i == 0 or arr[i][0] != arr[i-1][0]:
            ans = min(ans, max(area))
        
        # 만족할 경우 원래는 하나 줄이고 다른 부분은 늘린다.
        x, y = arr[i]
        if y > k:
            area[1] -= 1
            area[2] += 1
            # y = b 직선 위에 있다면 1 구역에서 2로 옮겨준다.
        else:
            area[4] -= 1
            area[3] += 1
            # y = b 직선 아래에 있다면 4 구역에서 3으로 옮겨준다.

print(ans)