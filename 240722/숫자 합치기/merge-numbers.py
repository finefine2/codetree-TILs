import heapq
n = int(input())
arr = list(map(int, input().split()))

arr.sort()
ans = 0
q = []

for k in arr:
    heapq.heappush(q, k)

while len(q) > 1:
    x1 = heapq.heappop(q)
    x2 = heapq.heappop(q)

    ans += x1 + x2
    heapq.heappush(q, x1 + x2)
    # heapq를 사용하면 더한 값을 새로 넣었을때
    # 만약 더한 값이 안에 있는 값보다 더 클 수도 있으니 heapq를 통하여 정렬해주어서
    # 다시 계산해주면서 진행해야 한다.

print(ans)