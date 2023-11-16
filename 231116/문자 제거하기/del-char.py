s = input() 

while len(s) > 1: 
    i = int(input()) 
    if i >= len(s): 
        s = s[:-1]
    else:
        s = s[:i] + s[i+1:]
    print(s)