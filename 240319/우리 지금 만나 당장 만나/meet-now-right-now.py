n = int(input())

pos = list(map(int, input().split()))
velo = list(map(int, input().split()))

def find(t):
    Max = pos[0] - velo[0] * t
    Min = pos[0] + velo[0] * t

    for i in range(1, n):
        x1 = pos[i] - velo[i] * t
        x2 = pos[i] + velo[i] * t

        Max = max(Max, x1)
        Min = min(Min, x2)
    
    return Max <= Min


left = 0
right = 1000000000
ans = 1000000000


for _ in range(100):
    mid = (left + right) / 2

    if find(mid):
        ans = min(ans, mid)
        right = mid
    else:
        left = mid
    
print(f"{ans:.4f}")