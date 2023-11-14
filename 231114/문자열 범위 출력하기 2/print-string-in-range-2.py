chrs = input() 
n = int(input()) 

if len(chrs) < n: 
    print(chrs) 
else: 
    print(chrs[-n:][::-1])