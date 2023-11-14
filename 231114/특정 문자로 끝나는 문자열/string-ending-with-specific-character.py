chars = [] 

for _ in range(10):
    chars.append(input()) 

input_x = input() 

cnt = 0 
for i in range(10): 
    if input_x == chars[i][-1]: 
        print(chars[i]) 
        cnt += 1

    if cnt == 0: 
        print("None")