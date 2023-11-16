chars = input() 
target = input() 

if target in chars:
    print(chars.index(target[0]))
else: 
    print(-1)