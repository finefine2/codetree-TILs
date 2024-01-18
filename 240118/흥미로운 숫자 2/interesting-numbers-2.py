'''
내 풀이가 더 깔끔 ㅎ 
'''
# X,Y = map(int,input().split()) 
# # 한 자리 '만' 다른 것을 어떻게 표현하지 
# def check_num(num): 
#     num_list = list(str(num)) 
#     check = len(num_list) - 1
#     num_a = num_list[0] 
#     num_b = num_list[1] 
#     if num_list.count(num_a) == check or num_list.count(num_b) == check: 
#         return True 

# ans = 0 
# for i in range(X,Y+1): 
#     if check_num(i): 
#         ans += 1
# print(ans) 

'''
given sol 
전체자릿수 - 1만큼 등장한 숫자를 찾으면 될거임 
'''
x,y = map(int,input().split()) 
ans = 0 
# 각 숫자 완탐 체크 
for i in range(x,y+1): 
    # digit 배열을 만들어 각 자리 숫자 개수 저장 
    # all_digits 에는 총 자릿수 개수 
    num = i 
    digit = [0] * 10 
    all_digits = 0 
    while(num): 
        digit[num % 10] += 1 
        all_digits += 1 
        num //= 10 
    # i가 흥미로우면 true, 아니면 false 
    interesting = False 
    # 흥미로운 수는 숫자 하나만 all_digits -1만큼 
    for j in range(10): 
        if digit[j] == all_digits - 1: 
            interesting = True 
    if interesting: 
        ans += 1 
print(ans)