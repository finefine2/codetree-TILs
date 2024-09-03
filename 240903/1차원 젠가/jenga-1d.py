N = int(input())

blocks = [int(input()) for _ in range(N)]
s1,e1 = tuple(map(int,input().split()))
s2,e2 = tuple(map(int,input().split()))

ans1 = []

for i in range(N):
    if s1-1 <= i < e1:
        continue
    else:
        ans1.append(blocks[i])
# print(ans1)

ans2 = []
for j in range(len(ans1)):
    if s2-1 <= j < e2:
        continue
    else:
        ans2.append(ans1[j])
print(len(ans2))
for a in ans2:
    print(a)