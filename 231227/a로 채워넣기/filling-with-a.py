# s = 'banana' 

# s = s[:2] + 'n' + s[3:] 
# print(s) 

s = input() 
s = s[:1] + 'a' + s[2:-2] + 'a' + s[-1] 
print(s)