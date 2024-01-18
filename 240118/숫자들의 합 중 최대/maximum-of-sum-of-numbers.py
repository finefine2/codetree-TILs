'''
my solution 
'''
# X,Y = map(int,input().split()) 
# ans = -1e9 
# def get_num(n): 
#     ans = 0
#     n_list = list(str(n)) 
#     for n in n_list: 
#         ans += int(n) 
#     return ans

# for i in range(X,Y+1): 
#     tmp = get_num(i)
#     ans = max(ans,tmp)
# print(ans) 

'''
given solution 
재귀함수를 이용한 각자리 수의 합 -> DigitSum
n 이 10보다 작으면 n 리턴 
n 이 10 이상이면 DigitSum(n//10) + (n%10) 
'''
x,y = map(int,input().split()) 

def digit_sum(n): 
    if n < 10: 
        return n 
    else: 
        return digit_sum(n//10) + (n%10) 
ans = 0 
# 각 자리 숫자 합 구하고 최댓값 갱신 
for i in range(x,y+1): 
    ans = max(ans,digit_sum(i)) 
print(ans)