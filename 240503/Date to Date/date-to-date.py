month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

m1, d1, m2, d2 = map(int, input().split())

answer = 0

if m1 == m2:
    answer = (d2 - d1) + 1
else:
    for i in range(m1, m2):
        answer += month[i]
    answer += (d2 - d1) + 1

print(answer)