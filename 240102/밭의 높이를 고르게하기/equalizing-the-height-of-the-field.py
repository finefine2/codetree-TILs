N,H,T = map(int,input().split())
nums = list(map(int,input().split())) 
# N 6 
# 길이 3 
# 부분집합 길이 3 
ans = 1e9 

def convert(arr): 
    global H
    cnt = 0  
    for a in arr: 
        if a != H: 
            cnt += abs(a-H) 
        elif a == H:
            continue 
    return cnt 
for i in range(len(nums)-T+1): 
    # 부분집합을 만든다 
    pos = nums[i:i+T]
    cnt = convert(pos)
    ans = min(cnt,ans) 
print(ans)