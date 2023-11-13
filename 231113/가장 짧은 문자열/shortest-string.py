a = input() 
b = input() 
c = input() 

if len(a) > len(b) > len(c): 
    print(len(a) - len(c))
elif len(a) > len(c) > len(b): 
    print(len(a) - len(b))
elif len(b) > len(a) > len(c): 
    print(len(b) - len(c))
elif len(b) > len(c) > len(a): 
    print(len(b)-len(a))
elif len(c) > len(a) > len(b):
    print(len(c)-len(b))
elif len(c) > len(b) > len(a):  
    print(len(c)-len(a))