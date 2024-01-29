N,K = map(int,input().split()) 
nums = list(int(input()) for _ in range(N)) 

def count_num(l,r): 
    cnt = 0 
    for n in nums: 
        if l <= n <= r: 
            cnt += 1 
    return cnt 
ans = 0 
# 크기가 K인 모든 구간을 잡아 해당 구간에 들어오는 숫자를 세어 그 중 최댓값 계산 
for i in range(1,10001): 
    ans = max(count_num(i,i+K)) 
print(ans)