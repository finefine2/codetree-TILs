# 선물 가격에만 쿠폰이 적용가능함 
N,B = map(int,input().split()) 
# class 사용은 나중으로.. 
class info: 
    def __init__(self,price,ship): 
        self.price = price
        self.ship = ship 
student = []
for _ in range(N): 
    price,ship = map(int,input().split()) 
    # student.append(info(price,ship)) 
    student.append([price,ship]) 
student.sort(key = lambda x:x[0])

# 예산 B가 선물비 + 배송비 합보다 작으면 되는 거 아닌가 
ans = 0 
for i in range(N): 
    # 쿠폰을 먹이는 건 오로지 하나 
    tmp = (student[i][0] // 2) + student[i][1] 
    cnt = 0 
    for j in range(N): 
        # 나머지 아이템들은 쿠폰을 안 먹이고 
        if j == i: 
            continue 
        tmp += student[j][0] + student[j][1] 
        cnt += 1 
        if tmp > B: 
            ans = max(ans,cnt) 
            break 
print(ans)