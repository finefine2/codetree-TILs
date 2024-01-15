N, B = map(int, input().split())
price_list = []
for _ in range(N):
    price = int(input())
    price_list.append(price)

# print(price_list)

# 예산 내 선물 가능한 최대 학생 수 구하기
def find_max(price_list, budget):
    sorted_list = sorted(price_list)

    # print(sorted_list)
    tot = 0
    for i in range(len(sorted_list)):
        tot += sorted_list[i]

        if tot > budget:
            index = i-1
            break
        
        index = i
    # print(index)
    return index
        
        

for i in range(N):
    # 쿠폰 적용할 선물 
    price_list[i] //= 2

    max_idx = 0
   
    idx = find_max(price_list, B)
    max_idx = max(idx, max_idx)

    price_list[i] *= 2

print(max_idx)