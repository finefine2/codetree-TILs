input_x = input()

for i in input_x: 
    if ('a' <= i <= 'z') or ('A' <= i <= 'Z') or ('0' <= i <= '9'): 
        print(i.lower(),end="")