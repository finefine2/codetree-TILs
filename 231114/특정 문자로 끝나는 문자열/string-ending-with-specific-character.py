chars = [] 

for _ in range(10):
    chars.append(input()) 

input_x = input() 

check_x = False
for i in range(10): 
    if input_x == chars[i][-1]:
        print(chars[i]) 
        check_x = True 
    else: 
        continue 
    
if check_x == False: 
    print("None")