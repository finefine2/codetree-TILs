N = int(input()) 
nums = [int(input()) for _ in range(N)] 
def carry(a,b,c): 
    max_len = max(len(str(a)), len(str(b)), len(str(c)))
    cnt = 0 
    while a > 0 or b > 0 or c > 0: 
        if (a % 10 + b % 10 + c % 10) >= 10: 
            break 
        elif (a % 10 + b % 10 + c % 10) < 10: 
            a //= 10 
            b //= 10 
            c //= 10
            cnt += 1
    if cnt == max_len: 
        return True 
    else: 
        return False

ans = -1
# 완탐 돌리기 
for i in range(N): 
    for j in range(i+1,N):
        for k in range(j+1,N): 
            if carry(nums[i],nums[j],nums[k]): 
                ans = max(ans, nums[i] + nums[j] + nums[k])
print(ans)