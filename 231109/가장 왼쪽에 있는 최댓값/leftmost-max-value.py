N = int(input()) 
nums = list(map(int,input().split())) 

prev_max_idx = N
# 첫 원소가 최대가 되기전까지 반복
while True: 
    # 최댓값 후보는 항상 첫번째부터 
    max_idx = 0 

    # 두 번째 원소부터 바로 직전 최대로 뽑힌
    # 원소 전까지 보면서 그 중 최대 index 갱신 
    # index 는 오름차순이기 때문에 
    # 최댓값이 여러 개인 경우 가장 왼쪽 원소가 뽑힘
    for i in range(1,prev_max_idx): 
        if nums[i] > nums[max_idx]: 
            max_idx = i 
    print(max_idx + 1, end=" ")

    # 최대인 원소가 첫 번째면 종료
    if max_idx == 0: 
        break 
    
    # 바로 직전 최대 index를 갱신 
    prev_max_idx = max_idx