N = int(input()) 
A = list(map(int,input().split())) 
B = list(map(int,input().split())) 

A.sort() 
B.sort() 

ans = True 
if A == B: 
    print("Yes") 
else: 
    print("No")