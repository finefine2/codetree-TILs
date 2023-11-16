# s = 'applebanana'
# length = len(s) 
# start_idx = -1 

# for i in range(length - 1): 
#     if s[i] == 'a' and s[i+1] == 'b': 
#         start_idx = i 
#         break 
# print(start_idx) 

# if 'ab' in s: 
#     print(s.index('ab'))
# else: 
#     print(-1) 

# print(s.find('ab'))

s, a = input().split() 

if a in s: 
    print(s.index(a))
else: 
    print("No")