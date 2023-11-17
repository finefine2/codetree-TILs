s,q = input().split() 
q = int(q) 

for _ in range(q): 
    quest = int(input()) 

    if quest == 1: 
        s = s[1:] + s[0] 
    elif quest == 2: 
        s = s[-1] + s[0:-1]
    elif quest == 3:
        s1 = s[0:len(s)//2] 
        s2 = s[len(s)//2:]
        s = s2[::-1] + s1[::-1]
    print(s)

'''
len(s) 4 
0 1 2 3 

3 2 1 0 

'''