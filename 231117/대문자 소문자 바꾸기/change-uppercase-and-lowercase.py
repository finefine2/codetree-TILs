input_x = input() 

# small letters (a - z)
# 97 ~ 122 

# capital letters (A - Z)
# 65 ~ 90 
ans = ""
for i in input_x:
    if 'a' <= i <= 'z': 
        ans += chr(ord(i) - 32) 
    else: 
        ans += chr(ord(i) + 32)
print(ans)