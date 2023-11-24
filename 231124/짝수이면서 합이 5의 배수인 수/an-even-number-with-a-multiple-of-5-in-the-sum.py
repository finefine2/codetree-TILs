'''
my solution

n = int(input()) 

def decide(num): 
    n_str = str(num)
    cnt = 0 
    ans = ""
    for n in n_str: 
        cnt += int(n) 
    if num%2 == 0 and cnt%5 == 0: 
        ans = "Yes"
    else: 
        ans = "No"
    return ans 

print(decide(n))
'''

# 짝수이며, 각 자리 숫자의 합이 5의 배수인지 판단 
# 주어지는 숫자는 전부 두 자리수 라는 조건을 기억 
n = int(input()) 

def is_magic_number(n): 
    return n % 2 == 0 and (n // 10 + (n%10)) % 5 == 0

if is_magic_number(n): 
    print("Yes")
else: 
    print("No")