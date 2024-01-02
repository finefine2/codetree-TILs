N = int(input()) 
a,b,c = map(int,input().split())
cnt = 0
def check_num(n,a,b,c): 
    if abs(n-a) < 2 or abs(n-b) < 2 and abs(n-c) < 2: 
        return True 
    else: 
        return False 

for i in range(1,N+1): 
    for j in range(1,N+1): 
        for k in range(1,N+1): 
            if check_num(i,a,b,c) or check_num(j,a,b,c) or check_num(k,a,b,c): 
                cnt += 1 
print(cnt)