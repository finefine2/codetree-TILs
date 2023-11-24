# def print_rect(n,m): 
#     for _ in range(n): 
#         print("*" * m) 
# r_num, c_num = map(int,input().split()) 
# print_rect(r_num,c_num)

def print_lines(n,m): 
    for _ in range(n): 
        print("*" * m) 
n,m = map(int,input().split()) 
print_lines(n,m)