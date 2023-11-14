n = int(input()) 

chars = [input() for _ in range(n)] 
input_x = input() 

cnt = 0 
le = 0 
for ch in chars: 
    if ch[0] == input_x: 
        cnt += 1  
        le += len(ch) 


print(f"{cnt} {le / cnt:.2f}")