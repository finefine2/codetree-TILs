n = int(input())

arr = []
for i in range(n):
    s, e = map(int, input().split())
    arr.append((s, e))

arr.sort(key=lambda x: x[1])

ans = 1
end = -1
for i in range(len(arr)-1):
    if end <= arr[i+1][0]:
        ans += 1
        end = arr[i+1][1]
        

print(ans)