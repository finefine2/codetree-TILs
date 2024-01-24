A,B,C = map(int,input().split()) 

ans = 0 
for i in range(1000):
    for j in range(1000):
        tmp = A * i + B * j 

        if tmp <= C: 
            ans = max(ans,tmp)
 
print(ans)