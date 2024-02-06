'''
각 상황에 대해 최선의 답이 될 가능성이 있는 후보들을 모두 열거하여 그 중 최선을 선택하게 하는 식으로 
진행을 하면 예외없이 비교적 깔끔하게 문제를 해결할 수 있게 됩니다. 
주어진 조건 하에서 일어날 수 있는 상황들을 모두 나열하여 정리하는 연습을 많이 해보는 것이 아주 중요
'''
N = int(input()) 
nums = list(map(int,input().split())) 
new_nums = nums 

new_nums.sort() 

# 먼저 가장 작은 수를 뽑아야 한다 
min_num = min(new_nums) 
tmp = [] 
for n in new_nums: 
    if n == min_num: 
        continue 
    tmp.append(n) 

second_num = min(tmp) 

cnt = []
ans = -1  
for i,n in enumerate(new_nums): 
    if n == second_num: 
        cnt.append(i+1) 

if len(cnt) != 1: 
    print(-1) 
elif len(cnt) == 1: 
    print(cnt[0])