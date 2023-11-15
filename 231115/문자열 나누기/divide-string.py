n = int(input()) 

chars = list(input().split()) 

chars_new = "".join(chars) 

for i in range(5): 
    print(chars_new[5*i:5*i+5])