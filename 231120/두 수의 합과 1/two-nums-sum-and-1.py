a,b = map(int,input().split())

a += b  

a_str = str(a) 
ans = 0 
for i in range(len(a_str)):
    if a_str[i] == "1": 
        ans += 1 
print(ans)