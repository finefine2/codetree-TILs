A = input() 
B = input() 

idx = 0 
while idx <= len(A) - len(B): 
    check = True 
    for j in range(len(B)): 
        if A[idx+j] != B[j]: 
            check = False 
            break 
    if check: 
        A = A[:idx] + A[idx+len(B):] 
        if idx != 0 and A[idx-1] == B[0]: 
            idx -= 2 
        else: 
            idx -= 1
    idx += 1 
print(A)