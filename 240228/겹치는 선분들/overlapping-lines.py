n, k = map(int, input().split())

x = 0
arr = []
for i in range(n):
    a, b = map(str, input().split())
    
    a = int(a)
    if b == 'L':
        arr.append((x - a, x))
        x -= a
    else:
        arr.append((x, x + a))
        x += a
    # 왼쪽일때는 왼쪽을 움직인 값으로 바꾸고
    # 오른쪽일때는 오른쪽을 움직인 값으로 바꾸어서
    # 선분의 시작과 끝을 나타내준다.

point = []
for a, b in arr:
    point.append((a, 1))
    point.append((b, -1))

point.sort()

# ans = 0
# s = 0
# for i, (x, v) in enumerate(point):
#     if s >= k:
#         prev, prev_v = point[i-1]
#         ans += x - prev_v
    
#     # k 이상일 경우에 ans를 더해준다. 전에거를 가져와서
    
#     s += v 

# print(ans)

ans = 0
s = 0
prev = None  # 이전 위치를 기억하기 위한 변수 추가
for i in range(len(point)):
    x, v = point[i]
    if prev is not None and s >= k:
        ans += x - prev  # 선분의 개수가 K 이상이면 길이를 더합니다.
    s += v 
    prev = x

print(ans)