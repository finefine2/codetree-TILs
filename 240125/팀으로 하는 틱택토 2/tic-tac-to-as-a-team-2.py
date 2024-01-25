nums = [] 
for i in range(3): 
    num = input()
    nums.append([num[0],num[1],num[2]])
# 같은 줄이어야 하고, 3 개 중 2개는 같은 숫자여야 함 

tmp = [[nums[0][0],nums[0][1],nums[0][2]], [nums[1][0],nums[1][1],nums[1][2]], [nums[2][0],nums[2][1],nums[2][2]],
        [nums[0][0],nums[1][0],nums[2][0]], [nums[0][1],nums[1][1],nums[2][1]], [nums[0][2],nums[1][2],nums[2][2]], 
        [nums[0][0],nums[1][1],nums[2][2]], [nums[0][2],nums[1][1],nums[2][0]]]
ans = 0 
def check(arr): 
    num1, num2, num3 = arr[0], arr[1], arr[2] 
    if num1 != num2 and num2 != num3 and num3 != num1: 
        return False 
    elif num1 == num2 and num2 == num3 and num3 == num1: 
        return False 
    else: 
        return True 

for t in tmp: 
    if check(t): 
        ans += 1 
print(ans)