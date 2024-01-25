N,M = map(int,input().split()) 
nums = [0] + list(map(int,input().split())) 
ans = 0 
# 어느 지점에서 시작할 지 전부 도전 
# 모든 경우에서 최대가 되는 수 계산 

for i in range(1,N+1): 
    sum_elem = 0 
    cur = i 
    # M move 
    for _ in range(M): 
        sum_elem += nums[cur] 
        cur = nums[cur] 
    ans = max(ans,sum_elem) 
print(ans)