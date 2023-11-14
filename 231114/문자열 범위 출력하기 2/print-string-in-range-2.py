chrs = input() 
n = int(input()) 

if len(chrs) < n: 
    print(chrs[::-1]) 
else: 
    print(chrs[-n:][::-1])