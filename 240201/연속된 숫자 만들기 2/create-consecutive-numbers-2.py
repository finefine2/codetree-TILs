A,B,C = map(int,input().split()) 

'''
A 가 BC 사이로 
C 가 AB 사이로 
'''

def check(a,b,c): 
    if b-a == 1 and c-b == 1: 
        return True 

if check(A,B,C): 
    print(0) 
else: 
    print(2)