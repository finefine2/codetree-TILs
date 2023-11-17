input_x = input() 

for i in input_x: 
    if ("a" <= i <= "z") or ("A" <= i <= "Z"): 
        print(i.upper(),end="")