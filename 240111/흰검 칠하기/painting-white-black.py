n = int(input())

arr1 = [0] * 200200
arr2 = [0] * 200200
color = [0] * 200200
# 흰색 검은색 각각 두 번 이상 칠해지면 회색

idx = 100000
for _ in range(n):
    a, b = map(str, input().split())
    if b == 'R':
        for i in range(idx, idx + int(a)):
            arr2[i] += 1
            color[i] = -1
        idx += int(a)
    else:
        for i in range(idx - int(a), idx):
            arr1[i] += 1
            color[i] = 1
        idx -= int(a)

white = 0
black = 0
gray = 0
for i in range(200000):
    if arr1[i] >= 2 and arr2[i] >= 2:
        gray += 1
    elif color[i] == 1:
        white += 1
    elif color[i] == -1:
        black += 1

print(white, black, gray)