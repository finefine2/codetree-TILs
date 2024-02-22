n, q = map(int, input().split())

dot = list(map(int, input().split()))

MAX = 1000000
arr = [0] * (MAX + 1)
pre_sum = [0] * (MAX+1)

for i in range(n):
    pre_sum[dot[i]] = 1

for i in range(1, MAX + 1):
    pre_sum[i] += pre_sum[i-1]

for i in range(q):
    a, b = map(int, input().split())
    if a == 0:
        print(pre_sum[b])
    else:
        print(pre_sum[b] - pre_sum[a-1])