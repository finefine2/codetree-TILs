# my solution 
# n1, n2 = map(int,input().split()) 
# A = list(map(int,input().split())) 
# B = list(map(int,input().split())) 

# def check_seq(s1,s2): 
#     for i in range(0,len(s1)-len(s2)+1): 
#         if s1[i:i+len(s2)] == s2: 
#             return True 
#     return False 

# def return_ans(A,B): 
#     if check_seq(A,B): 
#         print("Yes")
#     else: 
#         print("No") 

# return_ans(A,B)

# given solution 
n1,n2 = map(int,input().split()) 

a = list(map(int,input().split())) 
b = list(map(int,input().split())) 

# n 번 idx 부터 시작하는 n2 길이의 a수열과 b수열의 일치여부 체크 
def is_same(n): 
    for i in range(n2): 
        if a[i + n] != b[i]: 
            return False 
    return True 

# b 가 a의 연속부분수열인지? 
def is_subseq(): 
    for i in range(n1-n2+1): 
        if is_same(i): 
            return True 
    return False 

if is_subseq(): 
    print("Yes") 
else: 
    print("No")