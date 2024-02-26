n, q = map(int, input().split())

arr = list(map(int, input().split()))

L = [0] * (n+1)
R = [0] * (n+1)

L[0] = arr[0]
for i in range(1, n):
    L[i] = max(L[i-1], arr[i])

R[n-1] = arr[n-1]
for i in range(n-2, -1, -1):
    R[i] = max(R[i+1], arr[i])

# for i in range(n):
#     print(L[i], end = " ")
# print()
# for i in range(n):
#     print(R[i], end = " ")
# print()

for i in range(q):
    a, b = map(int, input().split())

    a -= 1
    b -= 1

    ans = 0
    ans = max(ans, L[a-1], R[b+1])

    print(ans)