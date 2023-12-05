'''
2진법으로 표현하기 

숫자를 계속 2로 나눠주며 몫과 나머지를 쭉 적어주는 식으로 표현 가능 
2로 계속 나눠주는 과정을 2보다 작아지기 전까지 반복하고 
몫이 1이 되는 순간에 멈춤 

결과적으로, 가장 끝에 적힌 몫에서부터 지금까지의 나머지들을 역순으로 적어주면 2진법이 됨 

'''
# n = 29 

# digits = [] 

# while True: 
#     if n < 2: 
#         digits.append(n)
#         break 
#     digits.append(n%2) 
#     n //= 2 

# # print binary number 
# for digit in digits[::-1]: 
#     print(digit,end="")

n = int(input())
ans = [] 

while True: 
    if n < 2: 
        ans.append(n)
        break 
    ans.append(n%2) 
    n //= 2 
for a in ans[::-1]: 
    print(a,end="")