n = int(input()) 

chars = list(input().split()) 

chars_new = "".join(chars) 
idx = len(chars_new) // 5 + 1 
for i in range(idx): 
    print(chars_new[5*i:5*i+5])