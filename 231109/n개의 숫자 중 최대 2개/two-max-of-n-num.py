N = int(input()) 
nums = list(map(int,input().split()))

# n 개 숫자가 순서대로 nums 배열에 담겼음 
# 현재 가장 큰 원소를 담을 변수 max1, 두 번째로 큰 원소 담을 변수 max2 

# 내림차순 정렬 후 첫 번째와 두 번째 원소는 다음과 같은 순서로 구할 수 있음 
# step1) nums[0], nums[1] 중 큰 원소를 max1, 나머지는 max2 

# step2) i >= 2에 해당하는 남은 원소들을 순서대로 보며 다음 규칙에 따라 max1, max2 갱신 
# - case1) nums[i] >= max1  --> max1 = nums[i], max2 = max1
# - case2) max1 > nums[i] > max2 = nums[i]

# Step1 
if nums[0] > nums[1]: 
    max1,max2 = nums[0], nums[1] 
else: 
    max2,max1 = nums[0], nums[1] 

# Step2: 3번째 원소부터 보면서 max1, max2 판단하기 
for i in range(2, N): 
    if nums[i] >= max1: 
        max2, max1 = max1, nums[i] 
    elif nums[i] > max2: 
        max2 = nums[i]
print(max1, max2)