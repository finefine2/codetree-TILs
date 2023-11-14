chars = list(input().split()) 

# for i in range(len(chars)): 
#     if i % 2 == 0:     
#         print(chars[i])

for i in range(0,len(chars),2):
    print(chars[i])