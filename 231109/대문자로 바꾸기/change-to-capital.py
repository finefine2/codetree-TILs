nums = []
for i in range(5): 
    nums.append(list(input().split()))

for i in range(5): 
    for j in range(3): 
        nums[i][j] = chr(ord(nums[i][j]) + ord('A') - ord('a'))
        print(nums[i][j], end=" ")
    print()