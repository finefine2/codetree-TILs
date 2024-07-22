# N = int(input()) 

# rest = list(map(int,input().split())) 

# L, T = map(int,input().split()) 


# ans = 0 

# # 먼저 팀장은 무조건 한명씩이라도 사용함 
# # 고객수는 레스토랑마다 존재함 
# for r in rest: 
#     # 오로지 한명 있는 팀장은 일단 제거 
#     r -= L
#     ans += 1 

#     # 만약 식당에 손님수가 남았다는 가정 하에 
#     if r > 0:
#         if r % T == 0: 
#             ans += (r // T)
#         else: 
#             ans += (r // T)  +1
# print(ans)

# 제공된 답안 
N = int(input()) 
customers = list(map(int,input().split())) 
leader_cap, member_cap = tuple(map(int,input().split())) 

def required_member_num(customer_num): 
    # 남은 고객이 없으면 검사 팀원은 ㄴㄴ 
    if customer_num <= 0:
        return 0 
    # 정확히 나누어떨어지면, 몫만큼의 인원이 필요 
    if customer_num % member_cap == 0: 
        return customer_num // member_cap
    # 나누어 떨어지지 않으면 1명이 더 필요 
    else: 
        return (customer_num // member_cap) + 1

ans = 0 
for customer_num in customers: 
    # 팀장 1명 필수 
    ans += 1 
    # 필요한 팀원 수만큼 더함 
    ans += required_member_num(customer_num - leader_cap) 
print(ans)