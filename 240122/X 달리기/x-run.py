x = int(input())

velo = 1
t = 0
dist = 0

import sys
Min = sys.maxsize
while True:
    dist += velo
    t += 1

    if dist == x:
        break

    # (1 + ... + (velo+1) )
    # 이거 보다 작을 경우 아직 남았으므로 속도 증가
    if dist <= x - (velo + 1)*(velo+2) / 2:
        velo += 1
    # (1 + ... + (velo) )
    # 이거보다 작을 경우에는 아직 유지
    elif dist <= x - (velo + 1) * velo / 2:
        continue
    else:
        velo -= 1
    # 아닌 경우에는 이제 속도 줄여야 한다.


print(t)