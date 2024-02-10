n = int(input())

arr = []
for i in range(n):
    tmp = list(map(int, input().split()))
    arr.append(tmp)

import sys
ans = sys.maxsize
check = [0] * (n+1)
def choose(num, start, total):
    global ans
    if num == n:
        ans = min(ans, total + arr[start][0])
        return

    for i in range(n):
        if check[i] == 0 and arr[start][i] > 0:
            check[i] = 1
            choose(num + 1, i, total + arr[start][i])
            check[i] = 0

choose(0, 0, 0)
print(ans)