n = int(input())


dp = [0] * 20

dp[0] = 1
dp[1] = 1
# dp[2] = 2
# dp[3] = 5
# 14
# 42

s = 1
for i in range(2, n+1):
    for j in range(i):
        dp[i] += dp[j] * dp[i-j-1]
        
# dp[i]에서 j개의 왼쪽 서브트리를 가지고 있고,
# i-j-1개의 노드를 오른쪽 서브르티로 가지는 경우를 모두 고려한다.

print(dp[n])