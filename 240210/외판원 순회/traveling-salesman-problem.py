n = int(input())

arr = []
for i in range(n):
    tmp = list(map(int, input().split()))
    arr.append(tmp)

import sys
ans = sys.maxsize
check = [0] * n
def choose(num, start, total):
    global ans
    if all(check):
        if arr[start][0] == 0:
            return

        ans = min(ans, total + arr[start][0])
        return

    for i in range(1, n):
        if arr[start][i] == 0 or check[i]:
            continue

        check[i] = 1
        choose(num + 1, i, total + arr[start][i])
        check[i] = 0

check[0] = 1
choose(0, 0, 0)
print(ans)