import heapq
n = int(input())
arr = list(map(int, input().split()))

q = []
s = arr[n-1]
ans = 0
heapq.heappush(q, arr[n-1])

for k in range(n-2, 0, -1):
    heapq.heappush(q, arr[k])
    # 뒤에서부터 넣어주면서 확인한다.
    
    s += arr[k]
    # 합도 뒤에서부터 추가해준다.
    # n-1번째는 위에서 미리 넣고 시작
    small = q[0]
    av = (s - small) / (n - k - 1)

    ans = max(ans, av)
        

print(f"{ans:.2f}")