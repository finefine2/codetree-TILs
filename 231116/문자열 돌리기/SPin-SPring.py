s = input() 
print(s) 
L = len(s)
while L > 0: 
    s = s[-1] + s[:-1]
    print(s)
    L -= 1