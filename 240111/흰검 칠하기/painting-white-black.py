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
            if arr1[i] >= 2 and arr2[i] >= 2:
                color[i] = 5
            else:
                color[i] = -1
        idx += int(a)-1
    else:
        for i in range(idx - int(a) + 1, idx+1):
            arr1[i] += 1
            if arr1[i] >= 2 and arr2[i] >= 2:
                color[i] = 5
            else:
                color[i] = 1
        idx -= int(a)-1

white = 0
black = 0
gray = 0
for i in range(len(color)):
    if color[i] == 5:
        gray += 1
    elif color[i] == 1:
        white += 1
    elif color[i] == -1:
        black += 1

print(white, black, gray)

# for i in range(99990,100010):
#     print(arr1[i], end = " ")

# for i in range(99990,100010):
#     print(arr2[i], end = " ")