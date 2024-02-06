'''
각 상황에 대해 최선의 답이 될 가능성이 있는 후보들을 모두 열거하여 그 중 최선을 선택하게 하는 식으로 
진행을 하면 예외없이 비교적 깔끔하게 문제를 해결할 수 있게 됩니다. 
주어진 조건 하에서 일어날 수 있는 상황들을 모두 나열하여 정리하는 연습을 많이 해보는 것이 아주 중요
'''
import sys 
N = int(input()) 
nums = list(map(int,input().split())) 
new_nums = sorted(nums) 
# 2번째로 작은 수가 존재 시 true 
isExist = False 
low2 = 0 
for elem in new_nums: 
    if elem != new_nums[0]: 
        low2 = elem 
        isExist = True 
        break 
# 2번째로 작은 숫자가 존재하지 않을 때 
if isExist == False: 
    print(-1)
    sys.exit() 

ansidx = -1 
for idx, elem in enumerate(new_nums): 
    if elem == low2: 
        if ansidx != -1: 
            print(-1) 
            sys.exit() 
        ansidx = idx 
print(ansidx + 1)