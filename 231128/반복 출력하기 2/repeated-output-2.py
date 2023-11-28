# def print_star(n): 
#     if n == 0: 
#         return 
#     print_star(n-1) 
#     print("*" * 5) 
# print("start") 
# print_star(3) 
# print("end")

def print_hello(n): 
    if n == 0: 
        return 
    
    print_hello(n-1)
    print("HelloWorld")

N = int(input())
print_hello(N)