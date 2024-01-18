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

# arr = []
# for i in range(3):
#     tmp = list(map(int, input()))
#     arr.append(tmp)

# ans = 0

# for i in range(1, 10):
#     for j in range(1, 10):
#         check = False
#         numi = 0
#         numj = 0

#         for k in range(3):
#             numi = 0
#             numj = 0
#             for l in range(3):
#                 if arr[k][l] == i:
#                     numi += 1
#                 if arr[k][l] == j:
#                     numj += 1
            
#             if numi + numj == 3 and numi >= 1 and numj >= 1:
#                 check = True
        
#         for k in range(3):
#             numi = 0
#             numj = 0
#             for l in range(3):
#                 if arr[l][k] == i:
#                     numi += 1
#                 if arr[l][k] == j:
#                     numj += 1
            
#             if numi + numj == 3 and numi >= 1 and numj >= 1:
#                 check = True
        
#         numi = 0
#         numj = 0
#         for k in range(3):
#             if arr[k][k] == i:
#                 numi += 1
#             if arr[k][k] == j:
#                 numj += 1
        
#         if numi + numj == 3 and numi >= 1 and numj >= 1:
#             check = True
        
#         numi = 0
#         numj = 0
#         for k in range(3):
#             if arr[k][2 - k] == i:
#                 numi += 1
#             if arr[k][2 - k] == j:
#                 numj += 1
        
#         if numi + numj == 3 and numi >= 1 and numj >= 1:
#             check = True
        
#         if check:
#             ans += 1
#             print(numi, numj)

# print(ans)