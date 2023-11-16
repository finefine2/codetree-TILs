s = input() 

target = s[1] 
change = s[0] 

s = list(s) 

for i in range(len(s)): 
    if s[i] == target: 
        s[i] = change

print("".join(s))