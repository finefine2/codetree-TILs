chars = input() 
c_list = list(chars)
for i in range(len(c_list)):
    if c_list[i] == 'e': 
        chars = chars[:i] + chars[i+1:]
        break 
print(chars)