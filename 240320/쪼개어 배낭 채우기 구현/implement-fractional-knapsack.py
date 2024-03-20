n, m = map(int, input().split())

arr = []
for i in range(n):
    a, b = map(int, input().split())
    arr.append((a, b))

arr.sort(key = lambda x : -x[1] / x[0])

ans = 0
for weight, value in arr:
    if m >= weight:
        m -= weight
        ans += value
    else:
        ans += (m / weight) * value
        break

print(f"{ans:.3f}")