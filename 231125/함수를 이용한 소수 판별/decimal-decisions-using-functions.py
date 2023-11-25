# 단, 하나라도 --> bool 타입 변수 선언하여 해결
# 이보다 깔끔한 건 함수 선언 

'''
소수 판별 
'''
def is_prime(n): 
    if n == 1: 
        return False 
    for i in range(2,n): 
        if n % i == 0: 
            return False 
    return True 

a,b = map(int,input().split()) 
ans = 0 

for i in range(a,b+1): 
    if is_prime(i): 
        ans += i 

print(ans)