s1,s2 = input().split()

n1 = ""
n2 = ""

cnt1 = 0 
cnt2 = 0
for i in range(len(s1)): 
    if "0" <= s1[i] <= "9": 
        n1 += s1[i] 
    else: 
        break

for i in range(len(s2)): 
    if "0" <= s2[i] <= "9": 
        n2 += s2[i] 
    else: 
        break
print(int(n1)+int(n2))