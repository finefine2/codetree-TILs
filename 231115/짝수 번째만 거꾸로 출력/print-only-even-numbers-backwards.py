# my solution
# A = input() 
# A_even = ""
# for i in range(1,len(A),2): 
#     A_even += A[i]

# print(A_even[::-1])

# suggestion 

A = input() 

# 가장 먼저 출력할 문자의 인덱스 
idx = len(A) - 1 
if idx % 2 == 0: idx -= 1

for i in range(idx,-1,-2): 
    print(A[i],end="")