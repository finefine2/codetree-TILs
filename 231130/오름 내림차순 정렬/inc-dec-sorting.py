n = int(input()) 
nums = list(map(int,input().split()))

nums.sort()
for num in nums: 
    print(num,end=" ")
nums.sort(reverse=True)
print()
for num in nums:
    print(num,end=" ")