class hand:
    def __init__ (self, time, a, b):
        self.time = time
        self.a = a
        self.b = b

n, k, p, t = map(int, input().split())

hands = []
for i in range(t):
    t, x, y = map(int, input().split())
    hands.append(hand(t, x, y))

arr = [0] * (n+1)
check = [0] * (n+1)

hands.sort(lambda x : x.time)
check[p] = True
for h in hands:
    aa = h.a
    bb = h.b

    if check[aa]:
        arr[aa] += 1
    if check[bb]:
        arr[bb] += 1
    
    if arr[aa] <= k and check[aa]:
        check[bb] = True
    if arr[bb] <= k and check[bb]:
        check[aa] = True
    
for i in range(1, n):
    if check[i]:
        print(1, end = "")
    else:
        print(0, end = "")


print(1)