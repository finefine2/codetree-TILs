n, m = map(int, input().split())

arr = list(map(int, input().split()))

ans = 0
for i in range(n):
    s = 0
    now = i
    for j in range(m):
        s += arr[now]
        now = arr[now] - 1
        # 값을 now라는 인덱스에 저장해서 계속 반복
    
    ans = max(ans, s)

print(ans)