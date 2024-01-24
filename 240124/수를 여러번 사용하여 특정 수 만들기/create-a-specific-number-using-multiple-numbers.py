A,B,C = map(int,input().split()) 
cntA = C // A 
cntB = C // B 
ans = 0 
for i in range(1,cntA + 1):
    for j in range(1,cntB + 1):
        tmp = A * i + B * j 

        if tmp <= C: 
            ans = max(ans,tmp)
        elif tmp > C: 
            break 
print(ans)