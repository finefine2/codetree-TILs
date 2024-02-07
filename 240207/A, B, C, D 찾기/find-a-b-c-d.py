n = 15

# 변수 선언 및 입력
arr = list(map(int, input().split()))

# 오름차순으로 정렬을 진행합니다.
arr.sort()

# 오름차순으로 정렬했을 때,
# 가장 작은 숫자는 A,
# 두 번째로 작은 숫자 B,
# 그리고 세 번째로 작은 숫자는 C가 됩니다.
a, b, c = arr[0], arr[1], arr[2]
# 또한, 가장 큰 숫자는 항상 A + B + C + D가 되므로
# D 는 끝 숫자 - A - B - C가 됩니다
d = arr[-1] - a - b - c

print(a, b, c, d)