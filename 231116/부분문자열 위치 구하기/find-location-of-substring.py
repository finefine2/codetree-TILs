chars = input() 
target = input() 

# if target in chars:
#     print(chars.index(target[0]))
# else: 
#     print(-1)

ans = -1
for i in range(len(chars)-1): 

    if chars[i:i+len(target)] == target: 
        ans = i 
        break 
print(ans)