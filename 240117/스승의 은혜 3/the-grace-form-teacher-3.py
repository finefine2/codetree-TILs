'''
my solution using sort function 
'''

# 선물 가격에만 쿠폰이 적용가능함 
# N,B = map(int,input().split()) 
# # class 사용은 나중으로.. 
# class info: 
#     def __init__(self,price,ship): 
#         self.price = price
#         self.ship = ship 
# student = []
# for _ in range(N): 
#     price,ship = map(int,input().split()) 
#     # student.append(info(price,ship)) 
#     student.append([price,ship]) 
# # student.sort(key = lambda x:x[0])
# student.sort(key = lambda x: (x[0]+x[1],-x[1]))

# # 예산 B가 선물비 + 배송비 합보다 작으면 되는 거 아닌가 
# ans = 0 
# for i in range(N): 
#     # 쿠폰을 먹이는 건 오로지 하나 
#     tmp = (student[i][0] // 2) + student[i][1] 
#     cnt = 0 
#     for j in range(N): 
#         # 나머지 아이템들은 쿠폰을 안 먹이고 
#         if j == i: 
#             continue 
#         tmp += student[j][0] + student[j][1] 
#         cnt += 1 
#         # print(f"coupon is applied for {i}")
#         # print(tmp,cnt) 
#         # print("########")
#         if tmp > B: 
#             ans = max(ans,cnt) 
#             break 
# print(ans) 

'''
given solution without sort
한 명씩 골라 선물 가격을 절반으로 적용하고 선물 가능한 학생의 최대 수를 구하기 
학생 한명을 골라 선물 가격을 절반으로 하고, 모든 가격을 오름차순으로 정렬한 뒤 
낮은 가격부터 더해가며, 예산을 넘지 않을 때까지 학생 수를 구하면, 최대 인원을 구할 수 있음
'''
N,B = map(int,input().split()) 
prices, ships = [],[]
for _ in range(N): 
    p,s = map(int,input().split())
    prices.append(p) 
    ships.append(s) 
ans = 0 
# 한 명에게 쿠폰을 쓸 때 선물 가능한 학생 최대 수
for i in range(N): 
    # i 번째 학생에게 쓸 떄 선물 가능한 수? 
    # tmp list 를 만들어 i번째 학생에게 쿠폰 적용 
    tmp = [0] * N 
    for j in range(N): 
        tmp[j] = prices[j] + ships[j] 
    tmp[i] = prices[j] // 2 + ships[j] 
    # 학생을 선물 가격 순 정렬 
    # 가격이 가장 작은 학생부터 사줄 때, 많은 학생에게 사줄 수 있음 
    tmp.sort() 
    student, cnt = 0,0 
    # 가장 많은 학생에게 선물 시, 학생 수 구하기 
    # studnet: 선물 받은 학생 수, cnt: 현재까지 사용금액 
    for j in range(N): 
        if cnt + tmp[j] > B: 
            break 
        cnt += tmp[j] 
        student += 1 
    ans = max(ans,student) 
print(ans)