N = int(input()) 
A = list(map(int,input().split())) 
B = list(map(int,input().split())) 

# A.sort() 
# B.sort() 

# 이게 답이 되네;

# if A == B: 
#     print("Yes") 
# else: 
#     print("No")

def compare(): 
    # n 개의 원소를 전부 비교하고 전부 같을 때만 일치, 단 하나라도 다르면 False
    for a,b in zip(A,B): 
        if a != b: 
            return False 
    return True 

A.sort() 
B.sort() 

if compare():
    print("Yes")
else:
    print("No")