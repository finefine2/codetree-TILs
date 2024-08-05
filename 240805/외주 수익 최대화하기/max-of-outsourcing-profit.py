N = int(input()) 
tasklist = [0] * N 
for i in range(N): 
    tasklist[i] = list(map(int,input().split())) 

def dfs(day,income): 
    global maxx 

    if day > N: 
        return 
    elif day == N: 
        maxx = max(maxx,income) 
        return 
    dfs(day+1,income) 
    dfs(day+tasklist[day][0],income+tasklist[day][1]) 
def main(): 
    global maxx 
    global N, tasklist
    maxx = -10 
    dfs(0,0) 
    print(maxx) 
main()