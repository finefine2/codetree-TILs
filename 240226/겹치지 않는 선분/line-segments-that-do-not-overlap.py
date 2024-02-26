n = int(input())

arr = []
for i in range(n):
    a, b = map(int, input().split())
    arr.append((a, b))

arr.sort()
L = [0] * (n+1)
R = [0] * (n+1)

l1, l2 = arr[0]
L[0] = l2

for i in range(1, n):
    a, b = arr[i]
    L[i] = max(L[i-1], b)
# L에는 끝점의 최대를 구해준다.

r1, r2 = arr[n-1]
R[n-1] = r2

for i in range(n-2, -1, -1):
    a, b = arr[i]
    R[i] = min(R[i+1], b)
# R에는 앞점의 최소들을 구해준다.

ans = 0
for i in range(n):
    a, b = arr[i]

    if i > 0 and L[i-1] >= b:
        continue
    if i < n-1 and R[i+1] <= b:
        continue
    
    # 만약 끝점의 최대가 b 이상일 경우 넘어간다.
    # 만약 앞점들의 최소가 b 이하일 경우 넘어간다.
    
    ans += 1

print(ans)