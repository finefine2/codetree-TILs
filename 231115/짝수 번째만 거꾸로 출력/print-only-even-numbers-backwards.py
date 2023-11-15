A = input() 
A_even = ""
for i in range(1,len(A),2): 
    A_even += A[i]

print(A_even[::-1])