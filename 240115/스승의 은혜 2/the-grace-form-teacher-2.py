from sys import stdin
n, b  = list(map(int, stdin.readline().split()))
base = [0 for _ in range(n)]
for i in range(n):
    base[i] = int(stdin.readline())//2
base.sort()
# print(base)

base = [0]+base
# print(base)
cnt = 0
total = 0
for i in range(1, n+1): #0을 더해서 예외처리가 필요없음!\
    total += base[i-1] + base[i]
    if total > b:
        break
    cnt += 1
print(cnt)