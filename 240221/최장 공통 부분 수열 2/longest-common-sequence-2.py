a = input()
b = input()

lena = len(a)
lenb = len(b)

# a = " " + a
# b = " " + b

dp = [[0] * (lenb + 1) for _ in range(lena + 1)]

for i in range(1, lena + 1):
    for j in range(1, lenb + 1):
        if a[i-1] == b[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

# for i in range(1, lena+1):
#     for j in range(1, lenb+1):
#         print(dp[i][j], end = " ")
#     print()


i, j = lena, lenb
st = []
while i > 0 and j > 0:
    if a[i-1] == b[j-1]:  # 문자가 같은 경우, 해당 문자를 결과에 추가하고 대각선으로 이동
        st.append(a[i-1])
        i -= 1
        j -= 1
    elif dp[i-1][j] > dp[i][j-1]:  # 위쪽이 더 큰 경우, 위로 이동
        i -= 1
    else:  # 왼쪽이 더 큰 경우, 왼쪽으로 이동
        j -= 1

print(''.join(reversed(st)))