str_A = input() 
ans = 0
for s in str_A: 
    if '0' <= s <= '9': 
        ans += int(s) 
print(ans)