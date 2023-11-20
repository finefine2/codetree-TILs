s1 = input() 
s2 = input() 

ans1 = "" 
ans2 = ""
for i in range(len(s1)): 
    if "0" <= s1[i] <= "9": 
        ans1 += s1[i] 
for j in range(len(s2)): 
    if "0" <= s2[j] <= "9": 
        ans2 += s2[j] 

print(int(ans1) + int(ans2))