N = int(input())
seats = list(input())

def cal_dist(string): 
    ans = 10000
    for i in range(len(string)): 
        for j in range(len(string)): 
            if i == j: 
                continue 
            if string[i] == '1' and string[j] == '1': 
                ans = min(ans,abs(i-j)) 
    return ans 
ans = 0
for i in range(N): 
    tmp = 0 
    if seats[i] == '0': 
        seats[i] = '1' 
        tmp = cal_dist(seats) 
        ans = max(tmp,ans) 
        seats[i] = '0'
print(ans)