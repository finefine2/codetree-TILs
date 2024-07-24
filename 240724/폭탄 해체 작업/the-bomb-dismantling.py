import heapq
n = int(input())

arr = []
for i in range(4):
    a, b = map(int, input().split())
    arr.append((b, a))
    # 시간제한, 점수

arr.sort()

q = []
idx = n-1
ans = 0

for t in range(10000, 0, -1):
    while idx >= 0 and arr[idx][0] >= t:
        heapq.heappush(q, -arr[idx][1])
        idx -=1 
    # 아직 idx가 0 이상이고, 시간제한이 아직 t이상일 경우에
    # heap에다가 점수를 내림차순으로 해주기 위해 -로 넣어준다.
    # push 해주었으므로 idx는 1 줄여줌
    
    if q:
        ans += -heapq.heappop(q)
    # q가 있을 경우에 for문의 한 차례에서 ans에 더해준다.

print(ans)