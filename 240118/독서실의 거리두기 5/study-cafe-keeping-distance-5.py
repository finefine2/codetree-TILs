# n = int(input())

# arr = input()
# for i in range(20):
#     arr += '2'

# import sys
# one = sys.maxsize
# idx = 0
# flag = False
# for i in range(n):
#     if arr[i] == '1':
#         if flag:
#            one = min(one, (i - idx))

#         flag = True
#         idx = i


# ans = 0
# for i in range(n):
#     dist = 0
#     if arr[i] == '0':
#         for j in range(1, n):
#             if i - j >= 0 and i + j < n:
#                 if arr[i-j] == '1' or arr[i+j] == '1':
#                     dist = j
#                     break
                    
#             elif i - j < 0 and i + j < n:
#                 if arr[i+j] == '1':
#                     dist = j
#                     break

#             elif i - j >= 0 and i + j >= n:
#                 if arr[i-j] == '1':
#                     dist = j
#                     break
#             else:
#                 break
#     ans = max(dist, ans)




# print(min(ans, one))


# 간단한 해설 풀이
n = int(input())
arr = list(input())

def find_dist():
    dist = n
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] == '1' and arr[j] == '1':
                dist = min(dist, j - i)
    return dist

ans = 0
for i in range(n):
    if arr[i] == '0':
        arr[i] = '1'
        ans = max(ans, find_dist())
        arr[i] = '0'
print(ans)