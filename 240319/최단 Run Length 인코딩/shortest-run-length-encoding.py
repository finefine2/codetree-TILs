A = input() 
def shift(A): 
    tmp = A[-1] 
    s = A[:-1]
    return tmp + s 

def run_length_encode(s): 
    ans = ""
    curr_char = s[0]
    num_char = 1 
    for sc in s[1:]: 
        if sc == curr_char: 
            num_char += 1 
        else: 
            ans += curr_char 
            ans += str(num_char) 

            curr_char = sc 
            num_char = 1 
    ans += curr_char
    ans += str(num_char) 
    return ans 

min_ans = len(run_length_encode(A))
i = 0 
while i <= len(A): 
    
    A = shift(A)
    min_ans = min(min_ans,len(run_length_encode(A))) 
    i += 1 
    # print(f"{i}th turn. string is {A} and length is {min_ans}")
print(min_ans)