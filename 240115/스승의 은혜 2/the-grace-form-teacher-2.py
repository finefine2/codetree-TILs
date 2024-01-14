import sys

N, B = map(int, input().split())
presents = sorted([int(input()) for _ in range(N)])

# 가장 비싼 선물을 반값으로 할인 받음
discounted = presents[-1] // 2

# 나머지 선물의 가격 합
rest = sum(presents[:-1])

# 선물을 줄 수 있는 학생 수
cnt = 0
budget = rest + discounted

# 예산이 충분하면 모든 학생에게 선물을 줄 수 있음
if budget <= B:
    cnt = N
# 예산이 부족하면 가장 싼 선물부터 주면서 예산을 초과하지 않는 선까지 선물을 줌
else:
    for i in range(N - 1):
        if budget - presents[i] > B:
            budget -= presents[i]
        else:
            cnt = i + 1
            break

print(cnt)