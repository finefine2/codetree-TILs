N = int(input())
circles = []
for _ in range(N): 
    circles.append(int(input()))

def repos(start,arr): 
    new_circles = arr[start:] + arr[:start] 
    return new_circles
ans = 1e9 

def cal_sum(arr): 
    ans = 0
    for i in range(1,len(arr)):
        ans += arr[i] * abs(i)
    return ans 
    
for i in range(N): 
    new_circles = repos(i,circles) 
    sum_num = cal_sum(new_circles)
    ans = min(sum_num,ans) 
print(ans)