n = int(input())

check = [0] * 101

for _ in range(n):
    a, b = map(int, input().split())
    for i in range(a, b+1):
        check[i] += 1

flag = False
for k in check:
    if k >= n:
        flag = True
    

if flag:
    print("Yes")
else:
    print("No")