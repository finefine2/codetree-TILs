X,Y = map(int,input().split()) 

# 한 자리 '만' 다른 것을 어떻게 표현하지 
def check_num(num): 
    num_list = list(str(num)) 
    check = len(num_list) - 1
    num_a = num_list[0] 
    num_b = num_list[1] 
    if num_list.count(num_a) == check or num_list.count(num_b) == check: 
        return True 

ans = 0 
for i in range(X,Y+1): 
    if check_num(i): 
        ans += 1
print(ans)