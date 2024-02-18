n = input()

MOD = 10 ** 9 + 7
leng = len(n)
arr = [1] * (leng + 1)
check = False
ans = 0
cnt = 0

dp = [[0] * 3 for _ in range(leng + 1)]

for i in range(1, leng + 1):
    arr[i] = (arr[i - 1] * 10) % MOD

for i in range(leng):
    num = int(n[i])

    for x in range(10):
        if x in [3, 6, 9]:
            ans += (dp[i][0] + dp[i][1] + dp[i][2]) * arr[leng - i - 1] % MOD
            ans %= MOD
        else:
            for k in range(3):
                dp[i + 1][(x + k) % 3] += dp[i][k]
                dp[i + 1][(x + k) % 3] %= MOD

    for x in range(num):
        if check or x in [3, 6, 9]:
            ans += arr[leng - i - 1] % MOD
            ans %= MOD
        else:
            dp[i + 1][(x + cnt) % 3] += 1
            dp[i + 1][(x + cnt) % 3] %= MOD

    if num in [3, 6, 9]:
        check = True
    else:
        cnt += num

if check:
    ans += 1
    ans %= MOD
else:
    dp[leng][cnt % 3] += 1
    dp[leng][cnt % 3] %= MOD

ans += dp[leng][0]
ans += (MOD - 1)
ans %= MOD

print(ans)






















# def find(num):
#     if num % 3 == 0:
#         return True
    
#     s = str(num)
#     flag = False
#     for k in s:
#         if k == '3' or k == '6' or k == '9':
#             flag = True
    
#     if flag:
#         return True
#     else:
#         return False