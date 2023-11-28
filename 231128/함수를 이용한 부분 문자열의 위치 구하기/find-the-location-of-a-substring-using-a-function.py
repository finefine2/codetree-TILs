# my sol
# in_s = input() 
# target = input() 
# ans = -1
# def check_s(): 
#     global in_s, target, ans
#     for i in range(len(in_s) - len(target)+1):
#         if target == in_s[i:i+len(target)]: 
#             ans = i 
#             break 

#     return False 
# check_s()
# print(ans)

text = input() 
target input() 

# 일치하는 문자열 판단 
def is_substr(start_idx): 
    n,m = len(text), len(target) 

    # 만약 text 길이를 넘게 되면 false 
    if start_idx + m - 1 >= n: 
        return False 
    # 하나라도 다르면 부분 문자열이 아님
    for j in range(m): 
        if text[start_idx+j] != target[j]: 
            return False 
    # 전부 일치하면 부분 문자열
    return True 

# 부분 문자열 위치를 return
def find_idx(): 
    n = len(text) 
    for i in range(n): 
        if is_substr(i):
            return i 
    return -1 
print(find_idx())