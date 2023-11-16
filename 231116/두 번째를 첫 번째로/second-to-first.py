# s = input() 

# target = s[1] 
# change = s[0] 

# s = list(s) 

# for i in range(len(s)): 
#     if s[i] == target: 
#         s[i] = change

# print("".join(s))

s = input() 

a,b = s[0], s[1] 

for i in range(len(s)): 
    if s[i] == b: 
        s = s[:i] + a + s[i+1:] 
print(s)