n = int(input())

arr = []
for i in range(n):
    s, e = map(int, input().split())
    arr.append((s, e))

arr.sort(key=lambda x: x[1])

ans = 0
end = -1
for s, e in arr:
    if end <= s:
        end = e
        ans += 1
        
print(ans)