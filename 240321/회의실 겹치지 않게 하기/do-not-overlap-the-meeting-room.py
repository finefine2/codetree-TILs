n = int(input())

arr = []
for i in range(n):
    s, e = map(int, input().split())
    arr.append((s, e))

arr.sort(key=lambda x : x[0])

ans = 100000

num = 0
end = 0
for s, e in arr:
    if end <= s:
        end = e
    else:
        num += 1

ans = min(ans, num)

arr.sort(key=lambda x : x[1])

num = 0
end = 0
for s, e in arr:
    if end <= s:
        end = e 
    else:
        num += 1

ans = min(ans, num)

print(ans)