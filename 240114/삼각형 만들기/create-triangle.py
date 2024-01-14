N = int(input()) 
points = [tuple(map(int,input().split())) for _ in range(N)] 

max_ans = -1e9 

def check(a,b,c): 
    r1,c1 = points[a]
    r2,c2 = points[b]
    r3,c3 = points[c]
    if (r1 == r2 and r2 == r3 and r3 == r1) or (c1 == c2 and c2 == c3 and c3 == c1): 
        return False
    elif (r1 == r2 or r2 == r3 or r3 == r1) and (c1 == c2 or c2 == c3 or c3 == c1): 
        return True 

def area(a,b,c): 
    r1,c1 = points[a] 
    r2,c2 = points[b]
    r3,c3 = points[c]
    n1 = r1*c2 + r2*c3 + r3*c1 
    n2 = r2*c1 + r3*c2 + r1*c3 

    return int(abs(n1-n2))

for i in range(N): 
    for j in range(i+1,N): 
        for k in range(N): 
            if k == i or k == j: 
                continue
            tmp = area(i,j,k)
            # if check(i,j,k): 
            #     tmp = area(i,j,k) 
            max_ans = max(max_ans,tmp) 
print(max_ans)