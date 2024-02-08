n = int(input())
arr = list(map(int, input().split()))

ans = 11
now = 0

def choose(now, cnt):
    global ans
    
    for i in range(1, arr[now] + 1):
        if now + i == n-1:
            ans = min(ans, cnt)
            return

        choose(now + i, cnt + 1)
    
choose(0, 1)
if ans == 11:
    print(-1)
else:
    print(ans)