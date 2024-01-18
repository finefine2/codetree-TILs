a, b, c = map(int, input().split())

Max = -1
# for i in range(1000):
#     for j in range(1000):
#         if a * i + b * j <= c:
#             Max = max(Max, a*i + b*j)

# 두번째 풀이 (정석)
for i in range(c // a + 1):
    num = a * i
    cnt = (c - num) // b
    num += cnt * b
    Max = max(Max, num)

print(Max)