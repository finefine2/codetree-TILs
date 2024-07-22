n, m = map(int, input().split())

arr = []
for i in range(n):
    w, v = map(int, input().split())
    arr.append((w, v))

arr.sort(key = lambda x : -x[1] / x[0])

ans = 0
for weight, value in arr:
    if m >= weight:
        ans += value
        m -= weight
    else:
        ans += (m / weight) * value
        break

print(f"{ans:.3f}")