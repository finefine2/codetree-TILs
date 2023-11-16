A = input()
B = input() 

'''
solution1. 
while A.find(B) != -1: 
    start = A.find(B) 
    A = A[:start] + A[start + len(B):] 
print(A) 
'''