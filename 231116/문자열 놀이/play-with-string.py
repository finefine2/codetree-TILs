s,q = input().split()
q = int(q) 
s_list = list(s) 
for _ in range(q): 
    q1,q2,q3 = input().split()

    if q1 == '1':
        s_list[int(q2)-1], s_list[int(q3)-1] = s_list[int(q3)-1], s_list[int(q2)-1] 
    elif q1 == '2': 
        for idx, s_ in enumerate(s_list): 
            if q2 == s_: 
                s_list[idx] = q3

    print("".join(s_list))