# s,q = input().split()
# q = int(q) 
# s_list = list(s) 
# for _ in range(q): 
#     q1,q2,q3 = input().split()

#     if q1 == '1':
#         s_list[int(q2)-1], s_list[int(q3)-1] = s_list[int(q3)-1], s_list[int(q2)-1] 
#     elif q1 == '2': 
#         for idx, s_ in enumerate(s_list): 
#             if q2 == s_: 
#                 s_list[idx] = q3

#     print("".join(s_list)) 

s,q = input().split()
q = int(q) 

for _ in range(q): 
    q1,a,b = input().split() 

    if int(q1) == 1: 
        a,b = int(a), int(b) 
        tmp = s[a-1] 

        s = s[:a-1] + s[b-1] + s[a:] 
        s = s[:b-1] + tmp + s[b:] 

        print(s)
    else: 
        for i in range(len(s)): 
            if s[i] == a: 
                s = s[:i] + b + s[i+1:]
        print(s)