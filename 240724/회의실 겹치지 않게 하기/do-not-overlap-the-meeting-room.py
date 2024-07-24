n = int(input())

arr = []
for i in range(n):
    a, b = map(int, input().split())
    arr.append((a, b))

arr.sort(key=lambda x : x[1])
# 끝나는 순으로 정렬한 다음에 앞에서부터 조건에 맞을 경우 차례대로 가져가면 된다.
ans = 0
end = 0
for k in arr:
    if k[0] >= end:
        end = k[1]
        ans += 1

print(n - ans)