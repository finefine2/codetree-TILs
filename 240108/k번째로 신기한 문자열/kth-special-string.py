n, k, t = map(str, input().split())

arr = []
for _ in range(int(n)):
    a = input()
    if a[0:len(t)] == t:
        arr.append(a)

arr.sort()
print(arr[int(k)-1])