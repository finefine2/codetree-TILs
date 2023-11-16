chars = input() 
target = input() 
ans = -1
for i in range(len(chars)-len(target)-1): 
    if chars[i:i+len(target)] == target: 
        ans = i 
        break 
print(ans)