import sys

n, m = map(int, input().split())

fire = list(map(int, input().split()))
station = list(map(int, input().split()))

ans = -1
fire.sort()
station.sort()

right = 0
for left in range(n):
    while right < m - 1 and abs(fire[left] - station[right]) >= abs(fire[left] - station[right+1]):
        right += 1
    
    ans = max(ans, abs(fire[left] - station[right]))

print(ans)