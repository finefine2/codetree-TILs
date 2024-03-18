n, t = map(int, input().split())

arr = []
for i in range(n):
    a = int(input())
    arr.append(a)

import sys
ans = sys.maxsize

import heapq
def find(num):
    q = []
    now = 0
    # 시작 시점

    for i in range(num):
        heapq.heappush(q, arr[i])
    for i in range(num, n):   # 먼저 끝나는 경우 끝내고 다음 순서를 넣는다.
        now = heapq.heappop(q)
        heapq.heappush(q, now + arr[i])
        # 현재까지 공연 시간 + 공연자 시간 : 총 공연시간
        # 즉 나온 heapq에 있는 값에다가 걸리는 시간을 더해서 넣어주면 그것의 끝나는 시간이 들어감 
    end = 0
    while q:    # 다 나올때까지 뽑으면서 가장 오래걸리는 값을 end로 찾는다.
        end = max(end, heapq.heappop(q))

    return end <= t

left = 1
right = n
ans = n

while left <= right:
    mid = (left + right) // 2

    if find(mid):
        ans = min(ans, mid)
        right = mid - 1
    else:
        left = mid + 1
    
print(ans)