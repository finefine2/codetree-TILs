# 내 풀이 
# num1, o, num2 = input().split() 

# def calc(num1,num2,o): 
#     ans = 0
#     num1 = int(num1) 
#     num2 = int(num2) 
    
#     if o == "+": 
#         return num1 + num2 
#     elif o == "-": 
#         return num1 - num2 
#     elif o == "/": 
#         return int(num1 / num2)
#     elif o == "*": 
#         return num1 * num2 
#     else: return False 

# ans = calc(num1,num2,o)
# if ans: 
#     print("{} {} {} = {}".format(num1,o,num2,ans))
# else: 
#     print("False")

'''
각 사칙연산을 구현
내 코드가 나은듯
'''
a,o,c = input().split() 
a = int(a) 
c = int(c) 

def plus(a,b): 
    return a + b 
def minus(a,b):
    return a - b 
def times(a,b): 
    return a * b 
def divide(a,b): 
    return a // b 

if o == "+": 
    print(a, "+", c, "=", plus(a,c))
elif o == "-": 
    print(a, "-", c, "=", minus(a,c))
elif o == "*": 
    print(a, "*", c, "=", times(a,c))
elif o == "/": 
    print(a, "/", c, "=", divide(a,c))
else: 
    print("False")