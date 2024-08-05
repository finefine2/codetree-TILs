N = int(input())
tasklist = [list(map(int, input().split())) for _ in range(N)]

income = [0] * (N+1)

for i in range(N):
    if i + tasklist[i][0] <= N: 
        income[i + tasklist[i][0]] = max(income[i+tasklist[i][0]],income[i] + tasklist[i][1]) 
    income[i+1] = max(income[i+1],income[i])
    
print(income[-1])