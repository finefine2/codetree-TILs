import heapq
n = int(input())

q = []
for i in range(n):
    arr = list(map(str, input().split()))
    if arr[0] == "push":
        heapq.heappush(q, -int(arr[1]))
    elif arr[0] == "size":
        print(len(q))
    elif arr[0] == "empty":
        if len(q) == 0:
            print(1)
        else:
            print(0)
    elif arr[0] == "top":
        print(-min(q))
    elif arr[0] == "pop":
        print(-heapq.heappop(q))