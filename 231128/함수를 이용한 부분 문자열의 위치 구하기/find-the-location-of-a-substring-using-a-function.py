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

#############################
# 변수 선언 및 입력:
text = input()
pattern = input()
# 일치하는 문자열인지를 판단합니다.
def is_substr(start_idx):
    n, m = len(text), len(pattern)
    
    # 만약 pattern을 매칭 시키기에
    # text 문자열 범위를 초과하게 된다면
    # 부분 문자열이 될 수 없으므로 false를 반환합니다.
    if start_idx + m - 1 >= n:
        return False

    for j in range(m):
        # 하나라도 다르다면, 부분 문자열이 아니므로 false를 반환합니다.
        if text[start_idx + j] != pattern[j]:
            return False

    # 전부 일치한다면 부분 문자열이므로 true를 반환합니다.
    return True

# 부분 문자열의 위치를 찾아 반환합니다.
def find_index():
    n = len(text)
    for i in range(n):
        # i번째를 시작으로 부분 문자열이 된다면, 해당 위치를 반환합니다.
        if is_substr(i):
            return i
    # 없다면, -1을 반환합니다.
    return -1
print(find_index())