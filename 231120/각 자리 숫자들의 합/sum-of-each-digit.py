n = int(input()) 
ans = 0 
n_str = str(n) 

for i in range(len(n_str)): 
    ans += int(n_str[i]) 

print(ans)