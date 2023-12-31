'''
생각의 흐름 
1. 10 - 99 사이 숫자를 일일이 잡아본다 
2. 숫자가 조건에 맞는지 확인하고, 그렇다면 개수 1 증가 
3. 답 출력 

pseudo code 1 
cnt = 0 
for i in range(10,100): 
    if is_magic_number(i): 
        cnt += 1 
print(cnt) 

is_magic_number 함수 
- 3의 배수가 아니면서 
- 각 자리 숫자가 다른 경우에만 magic_number 

def is_magic_number(n): 
    return n % 3 != 0 and all_different(n) 

def all_different(n): 
    return (n // 10) != (n % 10) 

이를 다 합친다면 

def all_different(n): 
    return (n // 10) != (n % 10) 

def is_magic_number(n): 
    return n % 3 != 0 and all_different(n) 

cnt = 0 

for i in range(10,100): 
    if is_magic_number(i): 
        cnt += 1

print(cnt) 
'''

'''
생각의 흐름 

1. 수를 센다 
2. 숫자에 3,6,9가 포함되어있거나 3의 배수이면 cnt를 늘린다 

for i in range(a,b+1): 
    if three_in or i % 3 == 0: 
        cnt += 1

def three_in(n):
    n_str = str(n) 
    if "3" in n_str or "6" in n_str or "9" in n_str: 
        return True 
    else: 
        return False 

'''
# 내 풀이 
# a,b = map(int,input().split())

# def three_in(n): 
#     n_str = str(n) 
#     if '3' in n_str or '6' in n_str or '9' in n_str: 
#         return True 
#     else: 
#         return False 
# cnt = 0 
# for i in range(a,b+1): 
#     if three_in(i) or i % 3 == 0: 
#         cnt += 1
# print(cnt)

a,b = map(int,input().split()) 

# 3,6,9 숫자가 하나라도 포함되어있는지 확인 
def check_369(n): 
    # 계속 10으로 나눠주며 일의 자리를 체크 
    while n > 0: 
        if n % 10 == 3 or n % 10 == 6 or n % 10 == 9: 
            return True
        n //= 10 
    return False 
# 3,6,9 를 포함하거나 3의 배수인지 판단 
def is_369_number(n): 
    return check_369(n) or (n % 3 == 0) 
cnt = 0 
for i in range(a,b+1): 
    if is_369_number(i):
        cnt += 1 
print(cnt)