N = int(input()) 
check = [5] * 101 
pige = []  
for i in range(N): 
    num, pos = map(int,input().split()) 
    pige.append((num,pos)) 
ans = 0
for p in pige: 
    if check[p[0]] == 5: 
        check[p[0]] = p[1] 
    else: 
        if check[p[0]] != p[1]: 
            ans += 1 
            check[p[0]] = p[1]
print(ans)