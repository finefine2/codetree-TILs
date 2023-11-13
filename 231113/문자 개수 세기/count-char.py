chars = input() 
pos = input() 
cnt = 0 

for elem in chars: 
    if elem == pos: 
        cnt += 1 
print(cnt)