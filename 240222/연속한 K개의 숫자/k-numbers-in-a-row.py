n, k, b = map(int, input().split())

pre_sum = [0] * (n+1)
arr = [0] * (n+1)
for i in range(b):
    a = int(input())
    arr[a] = 1

for i in range(1, n+1):
    pre_sum[i] = pre_sum[i-1] + arr[i]
# arr[i]가 0일 경우 별 차이 없이 그냥 지나가고
# 1일 경우에는 하나 증가된다.

import sys
ans = sys.maxsize
for i in range(1, n-k+2):
    ans = min(ans, pre_sum[i + k - 1] - pre_sum[i - 1])

# 여기서 pre_sum[i+k-1] - pre_sum[i-1]의 뜻은 k만큼의 간격을 가진 숫자들의 합을 구해줘서
# 추가해줘야 하는 숫자 개수를 바로 출력하는 것이다.

# 즉 구간합 중 최솟값을 구해주면 되는 것이다.
print(ans)