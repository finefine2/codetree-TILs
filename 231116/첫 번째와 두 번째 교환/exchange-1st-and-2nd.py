s = input() 

s_list = list(s) 
s1 = s[0] 
s2 = s[1] 
for i in range(len(s_list)): 
    if s_list[i] == s1: 
        s_list[i] = s2
    elif s_list[i] == s2: 
        s_list[i] = s1

print("".join(s_list))