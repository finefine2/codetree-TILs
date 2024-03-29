# ai = input()
# bi = input()

# a = " " + ai
# b = " " + bi
# lena = len(ai)
# lenb = len(bi)

# dp = [[0] * (lenb + 1) for _ in range(lena + 1)]

# if a[1] == b[1]:
#     dp[1][1] = 1
# else:
#     dp[1][1] = 2

# for i in range(2, lena + 1):
#     if a[i] == b[1]:
#         dp[i][1] = i
#     else:
#         dp[i][1] = dp[i-1][1] + 1

# for j in range(2, lenb + 1):
#     if a[1] == b[j]:
#         dp[1][j] = j
#     else:
#         dp[1][j] = dp[1][j-1] + 1

# for i in range(3, lena + 1):
#     for j in range(3, lenb + 1):
#         if a[i] == b[j]:
#             dp[i][j] = dp[i-1][j-1] + 1
#         else:
#             dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + 1

# if lena == 1 and lenb == 1:
#     if ai[0] == bi[0]:
#         print(1)
#     else:
#         print(0)
# else:
#     print(dp[len(ai)][len(bi)])

A = input()
B = input()

len_A = len(A)
len_B = len(B)

dp = [[0] * (len_B + 1) for _ in range(len_A + 1)]

for i in range(1, len_A + 1):
    for j in range(1, len_B + 1):
        if A[i - 1] == B[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(dp[len_A][len_B])