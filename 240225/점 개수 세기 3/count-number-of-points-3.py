from sortedcontainers import SortedSet

n, q = map(int, input().split())

arr = list(map(int, input().split()))

sort_arr = SortedSet(arr)
dic = dict()
num = 1

for k in sort_arr:
    dic[k] = num
    num += 1

for i in range(q):
    a, b = map(int, input().split())
    na, nb = dic[a], dic[b]
    print(nb - na + 1)