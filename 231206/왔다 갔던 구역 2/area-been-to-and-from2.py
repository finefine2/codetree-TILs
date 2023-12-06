# lines = [0] * 10000
# start = 5000
# N = int(input()) 

# for _ in range(N): 
#     x,d = input().split()
#     x = int(x) 
#     if d == "R": 
#         for i in range(start,start+x+1): 
#             lines[i] += 1
#         start = start + x
#     elif d == "L": 
#         for i in range(start,start-x-1,-1):
#             lines[i] += 1
#         start = start - x 
# cnt = [] 
# for i in range(len(lines)): 
#     if lines[i] >= 2: 
#         cnt.append(i) 
# ans = 0 

# for i in range(len(cnt)-1): 
#     if cnt[i+1] - cnt[i] == 1:
#         ans += 1
# print(ans)

# 각 이동마다 시작 - 도착점을 각각 배열에 표시해야 
# 그 후 원소 i에 대해 x1[i] ~ x2[i] 값까지 checked[] 에 표시

OFFSET = 1000
MAX_R = 2000 

n = int(input()) 
segments = [] 

curr =0 

for _ in range(n): 
    dist, direc = input().split()
    dist = int(dist) 

    if direc == "L": 
        # 왼쪽으로 이동: cur - dist ~ cur 까지 경로 이동 
        seg_left = curr - dist
        seg_right = curr
        cur -= dist 
    else: 
        # 오른쪽으로 이동: cur ~ cur + dist까지 경로 이동 
        seg_left = curr
        seg_right = curr + dist 
        cur += dist
    segments.append([seg_left,seg_right])
checked = [0] * (1 + MAX_R) 

for x1, x2 in segments: 
    # OFFSET을 더해줌 
    x1,x2 = x1 + OFFSET, x2 + OFFSET
    # 구간을 칠한다 
    for i in range(x1,x2): 
        checked[i] += 1 
# 2번 이상 지난 영역을 구함 
cnt = 0 
for c in checked: 
    if c >= 2: 
        cnt += 1 
print(cnt)