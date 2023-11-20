n, A = input().split()
ans = 0 
for _ in range(int(n)): 
    str_x = input() 
    if A == str_x: 
        ans += 1 
print(ans)