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


# 앞 부분은 Max, 뒷 부분은 Min 으로 해서 둘 중에 뒷 부분의 Min이 더 크면 교챠하는 식으로
# 하면 시간복잡도를 줄일 수 있을 것