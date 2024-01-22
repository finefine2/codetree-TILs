n, k = map(int, input().split())

arr = []
for i in range(n):
    a = int(input())
    arr.append(a)

bomb = [0] * 1000001
bomb_cnt = [0] * 1000001

for i in range(n):
    for j in range(i+1, min(i+k, n-1)):
        if arr[i] == arr[j]:
            bomb[i] = 1
            bomb[j] = 1

for i in range(len(bomb)):
    if bomb[i] != 0:
        bomb_cnt[arr[i]] += 1
        

Max = 0
Maxidx = 0
for i in range(n):
    if bomb[i]:
        if Maxidx < bomb_cnt[arr[i]]:
            Maxidx = bomb_cnt[arr[i]]
            Max = arr[i]

print(Max)   


# if not flag:
#     print(0)
# else:
#     print(Maxidx)