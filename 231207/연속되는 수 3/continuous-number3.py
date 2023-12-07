# 부호가 동일하면 곱했을 때 양수가 된다 
N = int(input()) 
nums = list(int(input()) for _ in range(N)) 
ans, cnt = 0,0 
for i in range(N): 
    if i >= 1 and nums[i] * nums[i-1] > 0:
        cnt += 1
    else: 
        cnt = 1
    ans = max(cnt,ans) 
print(ans)