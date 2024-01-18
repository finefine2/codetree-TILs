arr = []
for i in range(3):
    tmp = input()
    arr.append(tmp)

s = set()
for i in range(3):
    s1 = set()
    for j in range(3):
        s1.add(arr[i][j])
    if len(s1) == 2:
        s.add(tuple(sorted(s1)))

for i in range(3):
    s1 = set()
    for j in range(3):
        s1.add(arr[j][i])
    if len(s1) == 2:
        s.add(tuple(sorted(s1)))

s1 = set()
for i in range(3):
    s1.add(arr[i][i])
if len(s1) == 2:
    s.add(tuple(sorted(s1)))

s1 = set()
for i in range(3):
    s1.add(arr[i][2 - i])
if len(s1) == 2:
    s.add(tuple(sorted(s1)))

print(len(s))
# for k in s:
#     print(k)

# arr = []
# for i in range(3):
#     tmp = input()
#     arr.append(tmp)


# def checkline(line):
#     check = [0] * 9
    
#     for k in line:
#         check[int(k) - 1] += 1
    
#     # 1부터니까 1:로 해서 확인한다. 그리고 2가 넘는게 있으면 true
#     for k in check:
#         if k >= 2:
#             return True
#     return False

# ans = 0
# # 행
# for row in arr:
#     if checkline(row):
#         ans += 1
# # 열
# for col in range(3):
#     if checkline([arr[row][col] for row in range(3)]):
#         ans += 1
# # 대각선
# if checkline([arr[i][i] for i in range(3)]) or checkline([arr[i][2 - i] for i in range(3)]):
#     ans += 1

# print(ans)