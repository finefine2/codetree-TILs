'''
)((()())())
12
'''
A = input() 
ans = 0
for i in range(len(A)-1): 
    for j in range(i+1,len(A)-1): 
        if A[i] == "(" and A[i+1] == "(":
            if A[j] == ")" and A[j+1] == ")":
                ans += 1
print(ans)