N = int(input()) 

nums_A = list(map(int,input().split())) 
nums_B = list(map(int,input().split())) 
ans = 0 
for i in range(N): 
    if nums_A[i] > nums_B[i]: 
        num = nums_A[i] - nums_B[i] 
        nums_A[i] -= num 
        nums_A[i+1] += num 
        ans += num 
print(ans)